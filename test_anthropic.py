from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize client
client = Anthropic()

# Test message
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)