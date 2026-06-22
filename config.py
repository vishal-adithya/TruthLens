from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
    )

