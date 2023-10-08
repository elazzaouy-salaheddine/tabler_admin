from google.oauth2 import service_account
from googleapiclient.discovery import build
from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent
def get_calendar_events():
    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = os.path.join(BASE_DIR, 'google_client_secret.json')

    # Define the scopes you need for the Google Calendar API
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    # Authenticate
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    # Fetch calendar events (e.g., the next 10 events)
    events_result = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events
