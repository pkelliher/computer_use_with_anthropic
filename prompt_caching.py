from anthropic import Anthropic
from dotenv import load_dotenv
import os
import time

load_dotenv()

MODEL_NAME = "claude-sonnet-4-20250514"
MAX_TOKENS = 2048

client = Anthropic()

with open('files/frankenstein.txt', 'r') as file:
    book_content = file.read()

len(book_content)

book_content[1000:2000]

# # Uncached Request
# def make_non_cached_api_call():
#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "<book>" + book_content + "</book>"
#                 },
#                 {
#                     "type": "text",
#                     "text": "What happens in chapter 3?"
#                 }
#             ]
#         }
#     ]

def make_cached_api_call():
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "<book>" + book_content + "</book>",
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": "What happens in chapter 5?"
                }
            ]
        }
    ]

    start_time = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=500,
        messages=messages,
    )
    end_time = time.time()

    return response, end_time - start_time

# non_cached_response, non_cached_time = make_non_cached_api_call()
# print(f"Non-cached time: {non_cached_time:.2f} seconds")

# print("\nOutput (non-cached):")
# print(non_cached_response.content)

response1, duration1 = make_cached_api_call()
response1
response2, duration2 = make_cached_api_call()
response2.usage
duration2

response1, duration1 = make_cached_api_call()
print(f"First call duration: {duration1:.2f} seconds")
print(f"Response 1: {response1.content[0].text}\n")

response2, duration2 = make_cached_api_call()
print(f"Second call duration: {duration2:.2f} seconds")
print(f"Response 2 usage: {response2.usage}")
print(f"Cache hit! Duration difference: {duration1 - duration2:.2f} seconds")