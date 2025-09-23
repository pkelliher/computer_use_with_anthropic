from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "claude-sonnet-4-20250514"
MAX_TOKENS = 2048

client = Anthropic()

setting_the_role = """
You are an AI assistant specialized in analyzing customer reviews. 
Your task is to determine the overall sentiment of a given review 
and extract any specific complaints mentioned. 
Please follow these instructions carefully:
"""

instruction_pt1 = """
1. Review the following customer feedback:

<customer_review>
{{CUSTOMER_REVIEW}}
</customer_review>
"""

instruction_pt2 = """
2. Analyze the review using the following steps. 
Show your work in <review_breakdown> tags:

a) Key Phrase Extraction:
   - Extract and quote key phrases that indicate sentiment 
   (positive, negative, or neutral).
   - Extract and quote key phrases that suggest complaints or issues.

b) Sentiment Analysis:
   - Consider arguments for positive, negative, 
   and neutral sentiment based on the extracted phrases.
   - Determine the overall sentiment (positive, negative, or neutral) 
   based on your analysis.
   - Explain your reasoning for the sentiment classification.

c) Complaint Extraction:
   - List each specific issue or problem mentioned in the review.
   - For each complaint, provide the relevant quote from the review.
   - Count the total number of complaints found.

It's OK for this section to be quite long as you 
thoroughly break down the review.
"""

instruction_pt3 = """
3. Based on your analysis, 
generate a JSON output with the following structure:

<json>
{
  "sentiment_score": "Positive|Negative|Neutral",
  "sentiment_analysis": "Explanation of sentiment classification",
  "complaints": [
    "Complaint 1",
    "Complaint 2",
    "..."
  ]
}
</json>

If no complaints are found, 
use an empty array for the "complaints" field.

Remember:
- Base your analysis solely on the content of the provided review.
- Do not make assumptions or include information 
not present in the review.
- Be objective and focus on the customer's expressed 
opinions and experiences.
- Ensure your JSON output is properly formatted 
and contains all required fields.
"""

final_prompt = f"""
{setting_the_role}
{instruction_pt1}
{instruction_pt2}
{instruction_pt3}
"""

import re
def get_review_sentiment(review):
    #Insert the context into the prompt
    prompt = final_prompt.replace("{{CUSTOMER_REVIEW}}", review)
    # Send a request to Claude
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}        
        ]
    )
    output = response.content[0].text
    print("ENTIRE MODEL OUTPUT: ")
    print(output)
    
    sentiment = re.search(r'<json>(.*?)</json>', output, re.DOTALL)
    
    if sentiment:
        print("FINAL JSON OUTPUT: ")
        print(sentiment.group(1).strip())
    else:
        print("No sentiment analysis in the response.")

review1 = """
I am in love with my Acme phone.  It's incredible.
It's a little expensive, but so worth it imo.
If you can afford it, it's worth it! 
I love the colors too!
"""

get_review_sentiment(review1)