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
    image = image.resize((512, 512))
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    try:
        response = groq.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Describe the scene in this image. You are a personal robot for Mary..."
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

    except Exception as e:
        return f"[Error contacting vision model: {str(e)}]"