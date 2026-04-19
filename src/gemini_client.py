"""
Shared Gemini client singleton.
All modules import get_client() rather than re-initialising independently.
"""

import os
from google import genai

_client: genai.Client | None = None

EMBED_MODEL = "gemini-embedding-001"
GEN_MODEL   = "gemini-2.5-flash"


def get_client() -> genai.Client:
    """Return the module-level Gemini client, creating it on first call.

    Reads GEMINI_API_KEY from the environment.

    Returns:
        An initialised google.genai.Client instance.
    """
    global _client
    if _client is None:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")
        _client = genai.Client(api_key=api_key)
    return _client


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a list of strings using gemini-embedding-001.

    Args:
        texts: List of text strings to embed.

    Returns:
        List of embedding vectors (list of floats each).
    """
    client = get_client()
    result = client.models.embed_content(model=EMBED_MODEL, contents=texts)
    return [e.values for e in result.embeddings]


def embed_one(text: str) -> list[float]:
    """Embed a single string.

    Args:
        text: The text to embed.

    Returns:
        Embedding vector as a list of floats.
    """
    return embed_texts([text])[0]


def generate(prompt: str) -> str:
    """Generate a text response from gemini-2.5-flash.

    Args:
        prompt: The full prompt string.

    Returns:
        The model's text response.
    """
    client = get_client()
    response = client.models.generate_content(model=GEN_MODEL, contents=prompt)
    return response.text
