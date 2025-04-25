# app/utils/communicator.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt: str) -> str:
    response = groq.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()
