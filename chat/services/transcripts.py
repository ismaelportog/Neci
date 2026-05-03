import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = 30

def get_transcript(url: str) -> str:
    if not url:
        raise Exception("URL is required")
    
    if not url.startswith("http"):
        raise Exception("Invalid URL format")
    
    try:
        response = requests.get(
            f"{BASE_URL}/transcript",
            params={"url": url},
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        raise Exception("Request timed out")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch transcript: {e}")