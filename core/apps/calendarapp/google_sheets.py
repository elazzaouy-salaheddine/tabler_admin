# google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

def get_google_sheets_data():
    # Define the scope and credentials
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_SHEETS_API_JSON, scope)

    # Authenticate with the Google Sheets API
    client = gspread.authorize(creds)

    # Open the Google Sheets document by its title or URL
    sheet = client.open('Your Google Sheet Title or URL')

    # Select the specific worksheet within the document
    worksheet = sheet.get_worksheet(0)  # Change index as needed

    # Get data from the worksheet
    data = worksheet.get_all_records()

    return data
