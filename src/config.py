import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_INFO = {
    "type": "service_account",
    "project_id": os.getenv("GCP_PROJECT_ID"),
    "private_key_id": os.getenv("GCP_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GCP_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("GCP_CLIENT_EMAIL"),
    "client_id": os.getenv("GCP_CLIENT_ID"),
    "token_uri": "https://oauth2.googleapis.com/token",
}

API_BASE_URL = os.getenv("API_BASE_URL")
TOKEN_SHEET_ID = os.getenv("TOKEN_SHEET_ID")
CHAT_WEBHOOK_URL = os.getenv("CHAT_WEBHOOK_URL")

DATASET_IDS = {
    "dataset_1": os.getenv("DATASET_1_ID"),
    "dataset_2": os.getenv("DATASET_2_ID"),
    "dataset_3": os.getenv("DATASET_3_ID"),
    "dataset_4": os.getenv("DATASET_4_ID"),
}

# Target sheets (replace with your own)
SHEET_MAPPING = {
    "dataset_1": "SPREADSHEET_ID_1",
    "dataset_2": "SPREADSHEET_ID_2",
    "dataset_3": "SPREADSHEET_ID_3",
    "dataset_4": "SPREADSHEET_ID_4",
    "consolidated": "SPREADSHEET_ID_MASTER",
}
