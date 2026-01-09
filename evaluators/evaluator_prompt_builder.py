from config import prompts

def build_evaluator_prompt(evaluator_prompt, fabnav_prompt, requirements, user_input, maizey_output):
    
    return f""" [BEGIN EVALUATOR PROMPT] {evaluator_prompt} [END EVALUATOR PROMPT]
    [BEGIN SYSTEM PROMPT] {fabnav_prompt} [END SYSTEM PROMPT]
    [BEGIN REQUIREMENTS] {requirements} [END REQUIREMENTS]
    User Input: {user_input} Maizey Output: {maizey_output}"""