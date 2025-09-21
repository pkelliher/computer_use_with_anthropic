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

# print("Simple Chatbot (type 'quit' to exit)")
# # Store conversation history
# messages = []
# while True:
#     # Get user input
#     user_input = input("You: ")
#     # Check for quit command
#     if user_input.lower() == 'quit':
#         print("Goodbye!")
#         break
#     # Add user message to history
#     messages.append({"role": "user", "content": user_input})
#     try:
#         # Get response from Claude
#         response = client.messages.create(
#             model=MODEL_NAME,
#             max_tokens=200,
#             messages=messages
#         )
#         # Extract and print Claude's response
#         asst_message = response.content[0].text
#         print("Assistant:", asst_message)
        
#         # Add assistant response to history
#         messages.append({"role": "assistant", "content": asst_message})
        
#     except Exception as e:
#         print(f"An error occurred: {e}")

# #pre fill response, note assistant content value is omitted from response text.
# response = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=[
#         {"role": "user", "content": "Write a short poem about pigs"},
#         {"role": "assistant", "content": "Oink"}
#     ]
# )

# #without a stop_sequence
# prompt = """
# Generate a numbered, ordered list of technical topics 
# I should learn if I want to work on LLMs
# """
# response = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=[{"role": "user", "content": prompt}],
# )

# #With a stop_sequence, notice it stops at number 4, non inclusive, the stop_reason is stop_sequence when reviewing the full response.
# prompt = """
# Generate a numbered, ordered list of technical topics 
# I should learn if I want to work on LLMs
# """
# response = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     stop_sequences=["4."],
#     messages=[{"role": "user", "content": prompt}],
# )

# Temperature example, with temperatures of 0 and 1.
def demonstrate_temperature():
    temperatures = [0, 1]
    for temperature in temperatures:
        print(f"Prompting Claude three times with temperature of {temperature}")
        print("================")
        for i in range(3):
            response = client.messages.create(
                model=MODEL_NAME,
                max_tokens=100,
                messages=[{"role": "user", "content": f"Prompt {i+1}: Come up with a name for an alien planet. Respond with a single word."}],
                temperature=temperature
            )
            print(f"Response {i+1}: {response.content[0].text}")

demonstrate_temperature()

# print(message)
# print(message.content[0].text)
# print(response.content[0].text)