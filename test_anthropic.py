from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "claude-sonnet-4-20250514"
MAX_TOKENS = 1000

client = Anthropic()

# message = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=[
#         {"role": "user", "content": "Provide a brief definition of the top 5 prompting techniques"}
#     ]
# )

# message = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=[
#         {"role": "user", "content": "Hello! Only speak to me in French"},
#         {"role": "assistant", "content": "Bonjour!"},
#         {"role": "user", "content": "How are you?"}
#     ]
# )

print("Simple Chatbot (type 'quit' to exit)")
# Store conversation history
messages = []
while True:
    # Get user input
    user_input = input("You: ")
    # Check for quit command
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    try:
        # Get response from Claude
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=200,
            messages=messages
        )
        # Extract and print Claude's response
        asst_message = response.content[0].text
        print("Assistant:", asst_message)
        
        # Add assistant response to history
        messages.append({"role": "assistant", "content": asst_message})
        
    except Exception as e:
        print(f"An error occurred: {e}")

# print(message)
print(message.content[0].text)