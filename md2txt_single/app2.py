import os
import json
from openai import OpenAI



# === CONFIGURATION ===
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

input_folder = "/Users/ankitnayan/Downloads/ai_agent/md2txt_single/txt_files"
output_json_path = "/Users/ankitnayan/Downloads/ai_agent/cleaned_reviews.json"

system_prompt = """
You are a smart data cleaner.

Given a noisy product review page, extract only the clean structured data per review:
1. Product Name
2. Rating (out of 5)
3. Review Text

Ignore all ads, image links, HTML markup, or unrelated text.

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
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": raw_text}
                ],
                temperature=0.3
            )
            content = response.choices[0].message.content
            print("content", content)

            cleaned_content = extract_json(content)

            

            # reviews = json.loads(content)

            # print("######### reviews", reviews)
            # all_reviews.extend(reviews)

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

# # === OUTPUT ===
# with open(output_json_path, "w", encoding="utf-8") as out_file:
#     json.dump(all_reviews, out_file, indent=2, ensure_ascii=False)

# print(f"\n✅ Done. Total reviews extracted: {len(all_reviews)}")
# print(f"📁 Output written to: {output_json_path}")
