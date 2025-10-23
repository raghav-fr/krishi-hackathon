from functools import lru_cache
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
@lru_cache(maxsize=100)
def get_disease_details(disease_name: str):
    """Fetch structured plant disease info from Gemini."""
    prompt = f"""
    Provide information about the plant disease '{disease_name}'.
    Give the response strictly in JSON format with the following fields:
    {{
      "affected_plants": ["list of plants or crops affected"],
      "symptoms": "description of symptoms",
      "causes": "possible causes",
      "remedies": "how to prevent or treat the disease"
    }}
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:-3].strip()

        data = json.loads(text)
        return data

    except Exception as e:
        raise Exception(f"Gemini API error: {e}")

