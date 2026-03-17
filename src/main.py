from config import DATASET_IDS, SHEET_MAPPING, CHAT_WEBHOOK_URL, TOKEN_SHEET_ID
from sheets import get_token, write_sheet, sheets_service
from api import fetch_data
from utils import format_rows
import requests

DATASETS = ["dataset_1", "dataset_2", "dataset_3", "dataset_4"]

def notify(msg):
    if CHAT_WEBHOOK_URL:
        requests.post(CHAT_WEBHOOK_URL, json={"text": msg})

def run():
    token = get_token(TOKEN_SHEET_ID)

    # Process each dataset
    for name in DATASETS:
        print(f"Processing {name}")

        dataset_id = DATASET_IDS.get(name)
        sheet_id = SHEET_MAPPING.get(name)

        rows = fetch_data(
            dataset_id=dataset_id,
            endpoint="/api/data/{id}/query/csv",
            token=token
        )

        cleaned = format_rows(rows)
        success = write_sheet(sheet_id, cleaned)

        notify(f"{name}: {'updated' if success else 'failed'}")

    # Consolidation
    master_header = None
    merged = []

    for name in DATASETS:
        sheet_id = SHEET_MAPPING[name]

        res = sheets_service.spreadsheets().values().get(
            spreadsheetId=sheet_id,
            range="Sheet1!A1:ZZ"
        ).execute()

        values = res.get("values", [])
        if not values:
            continue

        header, body = values[0], values[1:]

        if master_header is None:
            master_header = header
            merged.append(header)

        for row in body:
            row += [""] * (len(header) - len(row))
            row_dict = dict(zip(header, row))
            merged.append([row_dict.get(col, "") for col in master_header])

    write_sheet(SHEET_MAPPING["consolidated"], merged)
    notify("consolidated updated")

if __name__ == "__main__":
    run()
