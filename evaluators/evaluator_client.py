from openai import OpenAI
import time

def create_client():
    return OpenAI()

def call_model(client, model, messages):
    for attempt in range(5):
        try:
            return client.chat.completions.create(
                model=model,
                messages=messages
            )
        except Exception as e:
            if attempt == 4:
                raise e
            time.sleep(2**attempt)

#Your evaluation code shouldn't know how retries or OpenAI API calls work