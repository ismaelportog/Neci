import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def get_transcript(url: str) -> dict:
    response = requests.get(
        f"{BASE_URL}/transcript",
        params={"url":url}
    )

    return response.text
