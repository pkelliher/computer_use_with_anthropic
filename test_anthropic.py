from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic()

# message = client.messages.create(
#     model="claude-sonnet-4-20250514",
#     max_tokens=500,
#     messages=[
#         {"role": "user", "content": "Provide a brief definition of the top 5 prompting techniques"}
#     ]
# )

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Hello! Only speak to me in French"},
        {"role": "assistant", "content": "Bonjour!"},
        {"role": "user", "content": "How are you?"}
    ]
)

print(message)
print(message.content[0].text)