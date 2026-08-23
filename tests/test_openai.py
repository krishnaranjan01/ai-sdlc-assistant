import os

from dotenv import load_dotenv
from openai import OpenAI


def test_openai():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5-mini",
        input="What is 2 + 2? Answer in one sentence."
    )

    print(response.output_text)

    assert response.output_text
