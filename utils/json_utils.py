import json, re

def extract_json(text):
    match = re.search(r"{.*}", text, re.S)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except:
        return None
    
#This prevents 90% of current pipeline crashes