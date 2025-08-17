# Ai_Text_Summarizer_App/frontend_app.py

# Streamlit frontend

import streamlit as st
from model import TextSummarizer

# Initialize summarizer
@st.cache_resource
def load_model():
    return TextSummarizer()

summarizer = load_model()

st.set_page_config(page_title="AI Text Summarizer", page_icon="✂️", layout="centered")
st.title("✂️ AI Text Summarizer")

user_input = st.text_area("Enter text to summarize:", height=200)

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer.summarize(user_input)
            st.subheader("Summary:")
            st.success(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize.")
