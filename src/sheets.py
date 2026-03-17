from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
import time

from config import SERVICE_ACCOUNT_INFO

creds = Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO)
sheets_service = build("sheets", "v4", credentials=creds)

def get_token(sheet_id):
    res = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range="sessionToken!A1"
    ).execute()

    return res["values"][0][0]

def write_sheet(spreadsheet_id, values, sheet_name="Sheet1", retries=3):
    if not values:
        return False

    try:
        sheets_service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1:ZZ100000"
        ).execute()
    except HttpError as e:
        if e.resp.status == 404:
            print(f"Sheet not found: {spreadsheet_id}")
            return False

    chunk_size = 1000

    for start in range(0, len(values), chunk_size):
        chunk = values[start:start + chunk_size]

        for i in range(retries):
            try:
                sheets_service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{sheet_name}!A{start+1}",
                    valueInputOption="USER_ENTERED",
                    body={"values": chunk}
                ).execute()
                break
            except HttpError as e:
                if e.resp.status == 404:
                    return False
                elif e.resp.status == 400:
                    print("Grid limit reached")
                    return False
                elif i < retries - 1:
                    time.sleep(3)
                else:
                    raise

    return True
