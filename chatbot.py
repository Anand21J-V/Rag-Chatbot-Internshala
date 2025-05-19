import os
import re
import pandas as pd
from dotenv import load_dotenv
from groq import Groq
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")

# Embedding wrapper
class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, show_progress_bar=False).tolist()

    def embed_query(self, text):
        return self.model.encode([text], show_progress_bar=False)[0].tolist()

class RAGChatbot:
    def __init__(self, groq_api_key, data_path):
        self.groq_client = Groq(api_key=groq_api_key)
        self.data_path = data_path
        self.embeddings = SentenceTransformerEmbeddings()
        self.vectorstore = None
        self.responses = []  # to store chat logs
        self._load_data_and_prepare()

    def _load_data_and_prepare(self):
        with open(self.data_path, 'r', encoding='utf-8') as f:
            text = f.read()

        product_chunks = re.findall(r'\d+\.\s+Product Name:.*?(?=(?:\n\d+\.|\Z))', text, re.DOTALL)
        docs = []

        for chunk in product_chunks:
            docs.append(Document(page_content=chunk.strip()))

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = splitter.split_documents(docs)

        self.vectorstore = FAISS.from_documents(split_docs, self.embeddings)

    def _groq_generate(self, prompt):
        response = self.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def answer_question(self, query):
        docs = self.vectorstore.similarity_search(query, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        answer = self._groq_generate(prompt)
        
        # Store the Q&A for logging
        self.responses.append({"Question": query, "Answer": answer})
        return answer

    def save_responses_to_excel(self, filename="chatbot_responses.xlsx"):
        if self.responses:
            df = pd.DataFrame(self.responses)
            df.to_excel(filename, index=False)

if __name__ == "__main__":
    data_path = "data/knowledge_base.txt"
    chatbot = RAGChatbot(groq_api_key, data_path)

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Saving conversation log to chatbot_responses.xlsx...")
                chatbot.save_responses_to_excel()
                print("Goodbye!")
                break
            response = chatbot.answer_question(user_input)
            print("Bot:", response)
    except KeyboardInterrupt:
        print("\nInterrupted. Saving responses...")
        chatbot.save_responses_to_excel()
