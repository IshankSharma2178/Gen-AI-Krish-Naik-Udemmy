import os
import streamlit as st  # type: ignore
from langchain_groq import ChatGroq  # type: ignore


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input
        self.model = None

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
            selected_groq_model = self.user_controls.get("selected_groq_model")

            if not groq_api_key or not selected_groq_model:
                st.error("Groq API Key and model must be provided.")
                return None

            self.model = ChatGroq(
                model=selected_groq_model,
                api_key=groq_api_key
            )
            return self.model

        except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            return None
