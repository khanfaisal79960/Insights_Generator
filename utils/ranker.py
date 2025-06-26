# utils/ranker.py
from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def analyze_raw_data(df):
    data_str = df.head(20).to_csv(index=False)

    prompt = f"""
You are a marketing analyst.

Here is a dataset of influencer campaign performance. The structure may vary across files:

{data_str}

Please analyze and answer:
1. Which 5 influencers are the most cost-effective?
2. Which ones should be scaled or paused?
3. Suggest 3 strategic optimization ideas based on trends in the data.
4. Give a clean, readable summary report suitable for managers.
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
