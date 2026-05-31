import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List available models
for m in genai.list_models():
    print(m.name)
