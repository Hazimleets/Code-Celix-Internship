# Ai_Text_Summarizer_App/model.py

# Handles text summarization (Hugging Face pipeline)

from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """Initialize the summarizer model"""
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text: str, max_len: int = 80, min_len: int = 30) -> str:
        """Generate summary for input text"""
        summary = self.summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return summary[0]['summary_text']
