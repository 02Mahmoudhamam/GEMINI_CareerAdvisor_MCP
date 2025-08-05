import os
import mimetypes
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def detect_content_type(file_path: str) -> str:
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        if mime_type.startswith("image"):
            return "image"
        elif mime_type.startswith("text") or mime_type == "application/pdf":
            return "text"
    return "unknown"


def generate_text_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text


def generate_multimodal_gemini(image_data, prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([image_data, prompt])
    return response.text
