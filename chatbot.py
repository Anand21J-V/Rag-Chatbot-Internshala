"""
RAG-based Chatbot using LangChain and Groq API
Author: Anand Vishwakarma
Date: 20-05-2025
"""

import pandas as pd
from langchain_community.document_loaders import CSVLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Groq
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Load data
def load_documents(file_path):
    loader = CSVLoader(file_path=file_path)
    documents = loader.load()
    return documents

# Embed and create vector store
def create_vectorstore(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# Setup LLM and RAG chain
def create_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = Groq(temperature=0, model_name="mixtral-8x7b-32768", api_key=groq_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

# Run chatbot
def ask_question(chain, question):
    response = chain.run(question)
    return response

if __name__ == "__main__":
    documents = load_documents("data/knowledge_base.csv")
    vectorstore = create_vectorstore(documents)
    qa_chain = create_rag_chain(vectorstore)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_question(qa_chain, user_input)
        print("Bot:", answer)
