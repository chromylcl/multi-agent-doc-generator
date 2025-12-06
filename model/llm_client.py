# model/llm_client.py

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads OPENAI_API_KEY from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system_prompt: str, user_message: str) -> str:
    """Call the chat model with a system + user message and return text content."""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # or any model you have access to
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content
