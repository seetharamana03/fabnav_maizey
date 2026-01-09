from utils.csv_utils import load_dataset, validate_columns
from utils.catalog_utils import load_catalog, compress_catalog
from evaluators.evaluator_prompt_builder import build_evaluator_prompt
from evaluators.evaluator_runner import score_response
from config.settings import MODEL_NAME, CATALOG_PATH
from config.prompts import FABNAV_SYSTEM_PROMPT, FABNAV_REQUIREMENTS, EVALUATOR_SYSTEM_PROMPT
import pandas as pd
import os
import json
from openai import OpenAI

def main():
    # catalog_df = load_catalog(CATALOG_PATH)
    # catalog_text = compress_catalog(catalog_df, keep_cols=["Machine","Material","Process","Tolerance","Training"])

    df = load_dataset("https://docs.google.com/spreadsheets/d/e/2PACX-1vTcFEHlemJJS6S0lzFuMHlSkv17_Wh3k_3PKJKrMpuHF7PJtDfcYKLvZCg_40iOGWL-plkHC82iRGc4/pub?gid=678653982&single=true&output=csv")
    df.columns = [c.encode('utf-8').decode('utf-8-sig').strip() for c in df.columns]
    validate_columns(df)

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    results = []
    for _, row in df.iterrows():
        prompt = build_evaluator_prompt(
            EVALUATOR_SYSTEM_PROMPT,
            FABNAV_SYSTEM_PROMPT,
            FABNAV_REQUIREMENTS,
            row["input"],
            row["output"]
        )

        score = score_response(client, MODEL_NAME, prompt)
        results.append(score)

    result_df = pd.json_normalize(results)
    result_df.to_csv("fabnav_evaluation_output.csv", index=False)

if __name__ == "__main__":
    main()
    # df = load_dataset("https://docs.google.com/spreadsheets/d/e/2PACX-1vTcFEHlemJJS6S0lzFuMHlSkv17_Wh3k_3PKJKrMpuHF7PJtDfcYKLvZCg_40iOGWL-plkHC82iRGc4/pub?gid=678653982&single=true&output=csv")
    # df.columns = [c.encode('utf-8').decode('utf-8-sig').strip() for c in df.columns]
    # print(df.columns)