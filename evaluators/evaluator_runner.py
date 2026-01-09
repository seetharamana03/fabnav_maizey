from config.prompts import EVALUATOR_SYSTEM_PROMPT
from utils.json_utils import extract_json
from evaluators.evaluator_client import call_model

def score_response(client, model, prompt):
    messages = [
        {"role": "system", "content": EVALUATOR_SYSTEM_PROMPT},
        {"role": "user",    "content": prompt}
    ]
    raw = call_model(client, model, messages)
    content = raw.choices[0].message.content
    data = extract_json(content)
    return data or {"final_score": 0, "comments": "Invalid JSON"}

#Runs a single evaluation and returns a parsed json
#This module ties in the system prompt, built prompt, model call and JSON extractor