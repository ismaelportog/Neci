import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

client = OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)


def load_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system.md")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def chat(messages: list[dict], transcripts: list[dict] = None, model: str = None):
    model = OLLAMA_MODEL

    system_prompt = load_system_prompt()

    if transcripts:
        context = "## Transcripciones disponibles:\n\n"
        for t in transcripts:
            context += f"### Fuente: {t['url']}\n{t['content']}\n\n"
        system_prompt = system_prompt + "\n\n" + context

    full_messages = [{"role": "system", "content": system_prompt}] + messages

    response = client.responses.create(
        model=model,
        input=full_messages,
        stream=True,
    )

    for event in response:
        if event.type == "response.output_text.delta":
            yield event.delta
