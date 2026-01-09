import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# -----------------------------
# SETTINGS
# -----------------------------
SPREADSHEET_ID = "1DzY4G55R-b_8byoJkKNh7JPTjV0cT5iIQjm7VT6uqe0"
SERVICE_ACCOUNT_FILE = "service_account.json"
SOURCE_TAB = "In Progress"

DESTINATION_TABS = {
    "binary": "Binary",
    "machine": "Machine Recommendation",
    "logistical": "Logistical",
    "safety": "Safety and Regulations",
    "process": "Multi-Step Process",
    "other": "Other"
}
# -----------------------------


def route_rows():
    # Authenticate
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
    client = gspread.authorize(creds)

    # Load sheet + source worksheet
    sheet = client.open_by_key(SPREADSHEET_ID)
    ws = sheet.worksheet(SOURCE_TAB)

    # Get all data
    rows = ws.get_all_values()
    headers = rows[0]
    data = rows[1:]  # exclude header

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)

    # For each question_type, move row to respective tab
    for idx, row in df.iterrows():
        qtype = row["Question Type"].strip().lower()

        if qtype not in DESTINATION_TABS:
            qtype = "other"

        dest_tab = DESTINATION_TABS[qtype]
        dest_ws = sheet.worksheet(dest_tab)

        # Append row to the destination tab
        dest_ws.append_row(row.tolist())

        print(f"Moved row {idx+2} → {dest_tab}")

    # OPTIONAL: Clear rows in In-Progress after routing
    ws.delete_rows(2, len(rows))

    print("Routing complete.")


if __name__ == "__main__":
    route_rows()
