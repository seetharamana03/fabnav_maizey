import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# -----------------------------
# SETTINGS
# -----------------------------
CSV_PATH = "fabnav_evaluation_output.csv"  # This CSV contains the evaluator output
SPREADSHEET_ID = ""     # Replace with your Google Sheet ID
WORKSHEET_NAME = "In Progress"               # The tab name in Google Sheets
SERVICE_ACCOUNT_FILE = "service_account.json"
# -----------------------------

def update_progress_sheet():
    # Load evaluator CSV
    df = pd.read_csv(CSV_PATH)

    # Authenticate credentials
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=scopes
    )
    client = gspread.authorize(credentials)

    # Open Google Sheet + Progress tab
    sheet = client.open_by_key(SPREADSHEET_ID)
    ws = sheet.worksheet(WORKSHEET_NAME)

    # Convert DataFrame columns to lists
    question_type = df["question_type"].tolist()
    completeness = df["completeness_score"].tolist()
    correctness = df["correctness_score"].tolist()
    reasoning = df["correctness_reasoning"].tolist()
    verified = ["Yes"] * len(df)

    # Determine starting row
    # Assumes row 1 is header → data starts at row 2
    start_row = 2

    # Write data to specific columns C–G
    ws.update(f"C{start_row}:C{start_row + len(question_type) - 1}",
              [[v] for v in question_type])

    ws.update(f"D{start_row}:D{start_row + len(completeness) - 1}",
              [[v] for v in completeness])

    ws.update(f"E{start_row}:E{start_row + len(correctness) - 1}",
              [[v] for v in correctness])

    ws.update(f"F{start_row}:F{start_row + len(reasoning) - 1}",
              [[v] for v in reasoning])

    ws.update(f"G{start_row}:G{start_row + len(verified) - 1}",
              [[v] for v in verified])

    print("Progress sheet updated successfully.")

if __name__ == "__main__":
    update_progress_sheet()
