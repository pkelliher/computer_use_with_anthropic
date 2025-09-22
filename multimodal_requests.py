from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "claude-sonnet-4-20250514"
MAX_TOKENS = 2048

client = Anthropic()


# messages = [
#     {
#         "role": "user",
#         "content": "tell me a joke"
#     }
# ]

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "tell me a joke"},
#         ]
#     }
# ]

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "who"},
#             {"type": "text", "text": "made"},
#             {"type": "text", "text": "you?"},
#         ]
#     }
# ]

# import base64
# # opens the image file in "read binary" mode
# with open("images/food.png", "rb") as image_file:
#     #reads the contents of the image as a bytes object
#     binary_data = image_file.read() 
#     #encodes the binary data using Base64 encoding
#     base_64_encoded_data = base64.b64encode(binary_data) 
#     #decodes base_64_encoded_data from bytes to a string
#     base64_string = base_64_encoded_data.decode('utf-8')


# messages = [
#     {
#         "role": "user",
#         "content": [{
#             "type": "image",
#             "source": {
#                 "type": "base64",
#                 "media_type": "image/png",
#                 "data": base64_string
#             },
#         },
#         {
#             "type": "text",
#             "text": """How many to-go containers of each type 
#             are in this image?"""
#         }]
#     }
# ]

# response = client.messages.create(
#     messages=messages,
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS
# )
# print(response.content[0].text)

# import base64
# import mimetypes

# def create_image_message(image_path):
#     # Open the image file in "read binary" mode
#     with open(image_path, "rb") as image_file:
#         # Read the contents of the image as a bytes object
#         binary_data = image_file.read()
#     # Encode the binary data using Base64 encoding
#     base64_encoded_data = base64.b64encode(binary_data)
#     # Decode base64_encoded_data from bytes to a string
#     base64_string = base64_encoded_data.decode('utf-8')
#     # Get the MIME type of the image based on its file extension
#     mime_type, _ = mimetypes.guess_type(image_path)
#     # Create the image block
#     image_block = {
#         "type": "image",
#         "source": {
#             "type": "base64",
#             "media_type": mime_type,
#             "data": base64_string
#         }
#     }
    
    
#     return image_block

# messages = [
#     {
#         "role": "user",
#         "content": [
#             create_image_message("./images/plant.png"),
#             {"type": "text", "text": "What species is this?"}
#         ]
#     }
# ]

# response = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=messages
# )
# print(response.content[0].text)

# messages = [
#     {
#         "role": "user",
#         "content": [
#             create_image_message("./images/invoice.png"),
#             {"type": "text", "text": """
#                 Generate a JSON object representing the contents
#                 of this invoice.  It should include all dates,
#                 dollar amounts, and addresses. 
#                 Only respond with the JSON itself.
#             """
#             }
#         ]
#     }
# ]

# response = client.messages.create(
#     model=MODEL_NAME,
#     max_tokens=MAX_TOKENS,
#     messages=messages
# )
# print(response.content[0].text)

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "write a poem"}],
    model=MODEL_NAME,
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)