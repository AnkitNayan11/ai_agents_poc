import os
import json
from openai import OpenAI

import re




# === CONFIGURATION ===
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

input_folder = "/Users/ankitnayan/Downloads/final_web_v1/web_crawl/scrapped_files_txt/"
output_json_path = "/Users/ankitnayan/Downloads/ai_agent/cleaned_reviews.json"

system_prompt = """
You are a smart data cleaner.

Given a noisy product review page, extract only the clean structured data per review:
1. Product Name
2. Rating (out of 5)
3. Review Text


Requirements:
- Remove all irrelevant content such as ads, HTML, links, non-text elements, and metadata.
- Ensure the output contains no emojis, special symbols, or formatting characters.
- Output clean, natural language in all fields.
- Remove all emojis and symbols like 👍🙂💯 from the review text and product names.
- Return the result as a valid JSON list, like:

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

# === PROCESSING ===
all_reviews = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        print(f"Processing: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                max_tokens= 10000,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": raw_text}
                ],
                temperature=0.3
            )
            content = response.choices[0].message.content
            print("content", content)

            

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

