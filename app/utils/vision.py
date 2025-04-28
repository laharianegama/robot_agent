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

def describe_image(image: Image.Image, current_task: str) -> str:
    # Resize image for faster sending (optional: adjust size if needed)
    image = image.resize((512, 512))

    # Convert image to base64
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
                            "text": (
                                f"As a personal robot for Mary, your task is to analyze if the user is working on the goal: '{current_task}'. "
                                "Describe ONLY the parts of the scene that are directly relevant to this task. "
                                "Ignore unrelated background or distractions. "
                                "Be concise (max 100 words). "
                                "Clearly mention whether Mary is making progress, has completed the task, or what step she still needs to complete."
                            )
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