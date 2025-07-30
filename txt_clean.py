import openai
from openai import OpenAI
import os

# Use the key from the global variable
api_key = os.getenv("OPENAI_API_KEY")

# Validate key presence
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Create the OpenAI client using the new API
client = OpenAI(api_key=api_key)

# Load raw text from the file
file_path = "/Users/ankitnayan/Downloads/ai_agent/webscraper_result/review_page_1.txt"

with open(file_path, "r", encoding="utf-8") as file:
    raw_text = file.read()

# System prompt
system_prompt = """
You are a smart data cleaner.

Given a noisy product review page, extract only the clean structured data per review:
1. Product Name
2. Rating (out of 5)
3. Review Text

Ignore all ads, image links, emojis, HTML markup, or unrelated text.

Return result as a JSON list like:
[
  {
    "product_name": "...",
    "rating": 5,
    "review": "..."
  },
  ...
]
"""

# Call OpenAI Chat API
response = client.chat.completions.create(
    model="gpt-4.1",
    max_tokens= 10000,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": raw_text}
    ],
    temperature=0.3
)

# Output result
print(response.choices[0].message.content)


