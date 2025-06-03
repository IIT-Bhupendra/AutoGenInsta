import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Your Perplexity API Key
# API_KEY = inputData['api_key']
API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("Please set the PERPLEXITY_API_KEY environment variable.")

# Perplexity API endpoint
API_URL = "https://api.perplexity.ai/chat/completions"

def call_perplexity(prompt: str, model: str = "sonar-pro", temperature: float = 0.5) -> str:
    """
    Makes a request to Perplexity API with a given prompt.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        raise Exception(f"API Request failed: {response.status_code}, {response.text}")