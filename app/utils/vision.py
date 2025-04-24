# app/utils/vision.py

import os
from dotenv import load_dotenv
from groq import Groq
import base64
from io import BytesIO
from PIL import Image

# Load API key
load_dotenv()
groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

def describe_image(image: Image.Image) -> str:
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Call Groq LLaVA-1.5
    response = groq.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the scene in this image. Be specific about emotion and location if possible."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{img_str}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content.strip()
