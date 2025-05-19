import streamlit as st

# Must be first
st.set_page_config(page_title="🤖 RAG Chatbot Assistant", layout="centered", page_icon="💬")

import os
from chatbot import RAGChatbot
from dotenv import load_dotenv
import time
import pandas as pd

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
data_path = "data/knowledge_base.txt"
excel_file = "chatbot_responses.xlsx"

# Custom CSS for styling
st.markdown("""
    <style>
        .chat-title {
            font-size: 2.2em;
            font-weight: bold;
            color: #3b82f6;
            margin-bottom: 10px;
        }
        .chat-subtext {
            color: #6b7280;
            font-size: 1.1em;
        }
        .stChatMessage {
            padding: 10px;
            border-radius: 12px;
        }
        .stChatMessage.user {
            background-color: #e0f2fe;
        }
        .stChatMessage.assistant {
            background-color: #fef3c7;
        }
        .dataframe th, .dataframe td {
            padding: 10px;
            font-size: 0.95em;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def get_chatbot():
    return RAGChatbot(groq_api_key, data_path)

chatbot = get_chatbot()

# Header
st.markdown('<div class="chat-title">RAG Chatbot Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-subtext">Ask about any product from the knowledge base below</div>', unsafe_allow_html=True)

# Chat history init
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"🧍‍♂️: {prompt}")

    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            time.sleep(0.8)
            response = chatbot.answer_question(prompt)
            st.markdown(f"🤖: {response}")

    st.session_state.messages.append({"role": "assistant", "content": response})
    chatbot.save_responses_to_excel(excel_file)

# Sidebar controls
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.success("Chat history cleared!")

    if st.button("View Saved Responses"):
        try:
            df = pd.read_excel(excel_file)
            st.markdown("### Saved Responses")
            st.dataframe(df, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading saved responses: {e}")

    st.markdown("---")
    st.markdown("Built by **Anand Kumar Vishwakarma**")
