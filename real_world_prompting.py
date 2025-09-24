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
review2 = """
I recently bought the ABC Smartwatch, and I have to say, it's been a 
bit of a rollercoaster. Let's start with the good stuff - 
the design is absolutely gorgeous. It's sleek, lightweight, 
and looks fantastic on my wrist. The display is crisp and bright, 
even in direct sunlight. I also love how customizable the watch 
faces are, allowing me to switch up the look whenever I want.
However, there are some significant downsides that I can't ignore. 
The battery life is terrible - I'm lucky if I get through a full 
day without needing to charge it. This is especially frustrating
when I'm traveling or out for long periods. The fitness tracking 
features, which were a big selling point for me, are hit or miss. 
It often doesn't accurately count my steps or calculate calories burned 
during workouts. Another issue I've encountered is with the touch 
sensitivity. Sometimes it's overly sensitive, registering accidental 
touches, while other times I have to tap multiple times for it to 
respond. It's inconsistent and annoying, especially when I'm trying to 
quickly check notifications or start a workout.On the plus side, the 
integration with my smartphone is seamless, and I appreciate being able 
to respond to texts and calls from my wrist. The water resistance has 
also held up well - I've worn it while swimming without any problems.
Customer service has been decent. They were quick to respond when I 
reported the battery issue, but their solution of turning off certain 
features defeats the purpose of having a smartwatch. All in all, while 
there are aspects of the ABC Smartwatch that I really like, the battery 
life and inconsistent performance are major drawbacks. For the price 
point, I expected better. It's not worth your money.
"""

get_review_sentiment(review2)