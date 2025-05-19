# streamlit_app.py

import streamlit as st
from chatbot import load_documents, create_vectorstore, create_rag_chain, ask_question

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("🔍 RAG-Based Chatbot with LangChain + Groq")

# Initialize
@st.cache_resource
def initialize_chain():
    docs = load_documents("data/knowledge_base.csv")
    vs = create_vectorstore(docs)
    return create_rag_chain(vs)

qa_chain = initialize_chain()

# Chat input
user_input = st.text_input("Ask a question:", key="user_input")

if user_input:
    response = ask_question(qa_chain, user_input)
    st.markdown(f"**Bot:** {response}")
