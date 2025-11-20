import pandas as pd
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  #api set in venv
in_progress_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTcFEHlemJJS6S0lzFuMHlSkv17_Wh3k_3PKJKrMpuHF7PJtDfcYKLvZCg_40iOGWL-plkHC82iRGc4/pub?gid=678653982&single=true&output=csv"
df = pd.read_csv(in_progress_url)


def score_maizey_response(input_text, maizey_output):
    """
    Sends input + Maizey's output to GPT as a judge.
    Returns a numeric score (1-10).
    """
    prompt = f"""
You are an expert familiar with the UMich Resource Catalog.
Input Question:
{input_text}

Maizey's Output:
{maizey_output}

On a scale from 1 to 10, score the response considering correctness, completeness, and clarity.
Only return the number.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    score = response.choices[0].message.content.strip()
    return score



#loops through spreadsheet response and scores them
scores = []
for idx, row in df.iterrows():
    input_text = row.get("input") or row.get("Input") or row.iloc[0] 
    maizey_output = row.get("output") or row.get("Output") or row.iloc[1] 
    input_preview = str(input_text)[:30] 
    print(f"Scoring row {idx+1}: {input_preview}...")    
    score = score_maizey_response(input_text, maizey_output)
    print("Score:", score)
    scores.append(score)

df['score'] = scores
df.to_csv("scored_maizey_output.csv", index=False)