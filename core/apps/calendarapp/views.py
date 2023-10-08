from django.shortcuts import render, redirect
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.http import JsonResponse
import json
from .google_sheets import get_google_sheets_data
import pandas as pd

def list_spreadsheets(request):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Drive API
    DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=DRIVE_SCOPES)
        drive_service = build('drive', 'v3', credentials=credentials)


        # List all spreadsheets in Google Drive
        results = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.spreadsheet'",
            fields="files(id, name)").execute()
        spreadsheets = results.get('files', [])

        return render(request, 'calendarapp/spreadsheets_list.html', {'spreadsheets': spreadsheets})

    except Exception as e:
        print(f"Error listing spreadsheets: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling


def get_spreadsheets_data(request, spreadsheet_id):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Sheets API
    SHEETS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SHEETS_SCOPES)
        service = build('sheets', 'v4', credentials=credentials)

        # Get information about the spreadsheet
        spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

        # Create a dictionary to store sheet names and their data
        sheets_data = {}

        # Loop through all sheets in the spreadsheet
        for sheet in spreadsheet['sheets']:
            sheet_name = sheet['properties']['title']

            # Get data from the current sheet
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=sheet_name).execute()
            sheet_data = result.get('values', [])

            # Store the sheet data in the dictionary
            sheets_data[sheet_name] = sheet_data

        return render(request, 'calendarapp/spreadsheet_data.html', {'sheets_data': sheets_data})

    except Exception as e:
        print(f"Error fetching spreadsheet data: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling



def get_all_sheets(request):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Sheets API
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=credentials)

        # Specify the spreadsheet ID
        spreadsheet_id = '17dRJuab2B3chiqtH8b7Pt2DxP8PCd9U3VLIPCVkp0cQ'

        # Get information about the sheets in the spreadsheet
        spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

        # Extract sheet names from the spreadsheet information
        sheet_names = [sheet['properties']['title'] for sheet in spreadsheet['sheets']]

        return render(request, 'calendarapp/sheets_list.html', {'sheet_names': sheet_names})

    except Exception as e:
        print(f"Error fetching sheet list: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling


def get_sheet_data(request, sheet_name):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Sheets API
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=credentials)

        # Specify the spreadsheet ID
        spreadsheet_id = '17dRJuab2B3chiqtH8b7Pt2DxP8PCd9U3VLIPCVkp0cQ'

        # Get data from the specified sheet
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=f'{sheet_name}!A1:Z100').execute()
        sheet_data = result.get('values', [])

        return render(request, 'calendarapp/sheet_data.html', {'sheet_data': sheet_data, 'sheet_name': sheet_name})

    except Exception as e:
        print(f"Error fetching sheet data: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling



def list_spreadsheets(request):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Drive API
    DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=DRIVE_SCOPES)
        drive_service = build('drive', 'v3', credentials=credentials)


        # List all spreadsheets in Google Drive
        results = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.spreadsheet'",
            fields="files(id, name)").execute()
        spreadsheets = results.get('files', [])

        return render(request, 'calendarapp/spreadsheets_list.html', {'spreadsheets': spreadsheets})

    except Exception as e:
        print(f"Error listing spreadsheets: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling


def get_spreadsheets_data(request, spreadsheet_id):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to your login view

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Sheets API
    SHEETS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SHEETS_SCOPES)
        service = build('sheets', 'v4', credentials=credentials)

        # Get information about the spreadsheet
        spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

        # Create a dictionary to store sheet names and their data
        sheets_data = {}

        # Loop through all sheets in the spreadsheet
        for sheet in spreadsheet['sheets']:
            sheet_name = sheet['properties']['title']

            # Get data from the current sheet
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=sheet_name).execute()
            sheet_data = result.get('values', [])

            # Store the sheet data in the dictionary
            sheets_data[sheet_name] = sheet_data

        return render(request, 'calendarapp/spreadsheet_data.html', {'sheets_data': sheets_data})

    except Exception as e:
        print(f"Error fetching spreadsheet data: {e}")
        # Handle the error as needed
        return render(request, 'error.html')  # You can create an 'error.html' template for error handling


def list_spreadsheets_json(request):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'})

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Drive API
    DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=DRIVE_SCOPES)
        drive_service = build('drive', 'v3', credentials=credentials)

        # List all spreadsheets in Google Drive
        results = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.spreadsheet'",
            fields="files(id, name)").execute()
        spreadsheets = results.get('files', [])

        # Create a list of dictionaries to store spreadsheet information
        spreadsheet_info = [{'id': sheet['id'], 'name': sheet['name']} for sheet in spreadsheets]

        # Return the spreadsheet_info list as a JSON response
        return JsonResponse({'spreadsheets': spreadsheet_info})

    except Exception as e:
        error_message = f"Error listing spreadsheets: {e}"
        return JsonResponse({'error': error_message})


def display_spreadsheets(request):
    # Fetch data from the list_spreadsheets view
    response = list_spreadsheets_json(request)
    data = response.content.decode('utf-8')  # Decode the JSON response

    # Parse the JSON data
    spreadsheets_info = json.loads(data)

    return render(request, 'calendarapp/spreadsheets_display.html', {'spreadsheets_info': spreadsheets_info})

def get_spreadsheets_data_json(request, spreadsheet_id):
    # Ensure the user is authenticated via OAuth 2.0
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'})

    # Your OAuth 2.0 credentials file (JSON)
    CREDENTIALS_FILE = 'service_account_django_tabler.json'

    # Define the scopes you need for the Google Sheets API
    SHEETS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SHEETS_SCOPES)
        service = build('sheets', 'v4', credentials=credentials)

        # Get information about the spreadsheet
        spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

        # Create a dictionary to store sheet names and their data
        sheets_data = {}

        # Loop through all sheets in the spreadsheet
        for sheet in spreadsheet['sheets']:
            sheet_name = sheet['properties']['title']

            # Get data from the current sheet
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=sheet_name).execute()
            sheet_data = result.get('values', [])


            # Store the sheet data in the dictionary
            sheets_data[sheet_name] = sheet_data

        # Pretty-print the sheets_data dictionary as JSON response
        pretty_sheets_data = json.dumps({'sheets_data': sheets_data}, indent=4)
        return JsonResponse(json.loads(pretty_sheets_data), safe=False)

    except Exception as e:
        error_message = f"Error fetching spreadsheet data: {e}"
        return JsonResponse({'error': error_message})


def display_spreadsheet_data(request, spreadsheet_id):
    # Fetch data from the get_spreadsheets_data_json view
    response = get_spreadsheets_data_json(request, spreadsheet_id)
    data = response.content.decode('utf-8')  # Decode the JSON response

    # Parse the JSON data
    spreadsheet_data = json.loads(data)

    return render(request, 'calendarapp/spreadsheet_json_data.html', {'spreadsheet_data': spreadsheet_data})


def import_data_from_google_sheets(request):
    google_sheets_data = get_google_sheets_data()

    # Process and populate your Django model with the fetched data
    # ...

    return JsonResponse({'message': 'Data imported successfully'})