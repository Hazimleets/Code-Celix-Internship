# Ai_Text_Summarizer_App/frontend_app.py

# Streamlit frontend

import streamlit as st
from model import TextSummarizer

# Initialize summarizer
summarizer = TextSummarizer()

# App config
st.set_page_config(page_title="AI Text Summarizer", page_icon="✂️", layout="wide")

# Sidebar
with st.sidebar:
    st.title("📘 About")
    st.info(
        "This AI Text Summarizer uses **Hugging Face Transformers** "
        "to condense long text into concise summaries.\n\n"
        "🔹 Enter text in the box\n"
        "🔹 Click 'Summarize'\n"
        "🔹 Get your summary instantly"
    )
    st.markdown("---")
    st.caption("👨‍💻 Developed for Code-Celix Internship Project")

# Main Title
st.markdown(
    """
    <div style="text-align: center;">
        <h1>✂️ AI Text Summarizer</h1>
        <p style="font-size:18px; color:gray;">
            Summarize long paragraphs into clear, concise lines instantly
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input section
st.markdown("### 📝 Enter your text below:")
user_input = st.text_area("Input Text", height=200, placeholder="Paste or type your text here...")

# Button + Output
if st.button("✨ Summarize Text", use_container_width=True):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer.summarize(user_input)

        # Display output in a styled box
        st.markdown("### 📌 Summary Result:")
        st.success(summary)
    else:
        st.warning("⚠️ Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "⚡ Powered by Hugging Face | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
