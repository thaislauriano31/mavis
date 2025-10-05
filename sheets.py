import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def get_sheets_service():
    creds = Credentials.from_service_account_file(
        os.getenv("SHEETS_KEYS"),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)

def get_sheet_values(range):
    service = get_sheets_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=os.getenv("SHEET_ID"),
        range=range
    ).execute()
    return result.get("values", [])

def update_sheet_values(range, values):
    service = get_sheets_service()
    body = {
        "values": values
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=os.getenv("SHEET_ID"),
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()
    return result.get("updatedCells", 0)
