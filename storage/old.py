import streamlit as st
import os
from dotenv import load_dotenv
import uuid

# Import from our modules
from models.model_loader import load_models
from models.classifier import create_classifier_chain
from chains.chain_builder import create_legal_chain
from storage.vector_store import ChatHistoryStore
from utils.helpers import format_message, create_empty_files

# Create necessary directory structure and files
create_empty_files()

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Legal Chatbot",
    page_icon="⚖️",
    layout="wide",
)

# Initialize session state
if "models" not in st.session_state:
    with st.spinner("Loading models..."):
        st.session_state.models = load_models()
        
if "classifier_chain" not in st.session_state:
    with st.spinner("Initializing classifier..."):
        st.session_state.classifier_chain = create_classifier_chain(st.session_state.models["llama"])

if "legal_chain" not in st.session_state:
    with st.spinner("Building chains..."):
        st.session_state.legal_chain = create_legal_chain(
            st.session_state.models, 
            st.session_state.classifier_chain
        )

if "history_store" not in st.session_state:
    st.session_state.history_store = ChatHistoryStore()

if "session_id" not in st.session_state:
    st.session_state.session_id = st.session_state.history_store.create_new_session()

if "messages" not in st.session_state:
    st.session_state.messages = []

# UI Components
st.title("⚖️ Legal Chatbot")

# Sidebar
with st.sidebar:
    st.header("Session Management")
    
    if st.button("New Session"):
        # Create new session
        st.session_state.session_id = st.session_state.history_store.create_new_session()
        st.session_state.messages = []
        st.success("New session created!")
    
    st.divider()
    st.subheader("About")
    st.markdown("""
    This chatbot is specialized in answering legal questions. It uses a classifier to determine
    if your query is legal in nature and routes it to the appropriate model.
    
    **Note:** This is for informational purposes only and not a substitute for legal advice.
    """)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(f"{message['content']}")

# Chat input
if prompt := st.chat_input(str("Ask a legal question...")):
    # Add user message to state and display
    st.session_state.messages.append(format_message("user", prompt))
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add to vector store
    st.session_state.history_store.add_message(st.session_state.session_id, "user", prompt)
    
    # Get chat history
    chat_history = st.session_state.history_store.get_chat_history(st.session_state.session_id)
    
    # Process with the chain
    with st.spinner("Thinking..."):
        response = st.session_state.legal_chain.invoke({
            "user_input": prompt,
            "chat_history": chat_history
        })
    
    # Add assistant message to state and display
    st.session_state.messages.append(format_message("assistant", response))
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
    
    # Add to vector store
    st.session_state.history_store.add_message(st.session_state.session_id, "assistant", response)

# Run the app with: streamlit run app.py