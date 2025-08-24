import streamlit as st
import os
from dotenv import load_dotenv

# Import from our modules
from models.model_loader import load_models
from models.classifier import create_classifier_chain
from chains.chain_builder import create_legal_chain
from utils.helpers import create_empty_files
from complaint_form.complaint_form_ui import complaint_form
from complaint_form.auto_complaint import run_automatic_complaint

# Create necessary directory structure and files
create_empty_files()

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="LexAI Assistant",
    page_icon="⚖️"
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

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar with navigation
with st.sidebar:
    st.title("Options")
    menu = st.radio("Navigation", ["LexAI Chat", "Automatic Complaint"])

    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.write("For informational purposes only. Not legal advice.")

# LexAI Chat page
if menu == "LexAI Chat":
    st.title("LexAI Assistant")

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write("You: " + message["content"])
        else:
            st.write("LexAI: " + message["content"])

    def process_input():
        user_input = st.session_state.user_input
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            response = st.session_state.legal_chain.invoke({
                "user_input": user_input,
                "chat_history": ""
            })
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.user_input = ""
            st.rerun()

    st.text_input("Ask a legal question:", key="user_input", on_change=process_input)
    st.button("Send", on_click=process_input)

# Automatic Complaint form page
elif menu == "Automatic Complaint":
    st.title("📝 File an Automatic Complaint")
    data = complaint_form()
    if data:
        run_automatic_complaint()
        st.success("✅ Complaint process initiated successfully!")
        st.balloons()