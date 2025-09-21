from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "claude-sonnet-4-20250514"
MAX_TOKENS = 1000

client = Anthropic()


messages = [
    {
        "role": "user",
        "content": "tell me a joke"
    }
]

response = client.messages.create(
    messages=messages,
    model=MODEL_NAME,
    max_tokens=MAX_TOKENS
)
print(response.content[0].text)