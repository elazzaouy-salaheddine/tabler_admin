from django.urls import path
from . import views

urlpatterns = [
    path('sheets-list/', views.get_all_sheets, name='sheets_list'),
    path('sheets-list/<str:sheet_name>/', views.get_sheet_data, name='sheet_data'),
    path('spreadsheets-list/', views.list_spreadsheets, name='spreadsheets_list'),
    path('spreadsheets-list/<str:spreadsheet_id>/', views.get_spreadsheets_data, name='spreadsheets_data'),

    path('spreadsheets-list-json/', views.list_spreadsheets_json, name='get_spreadsheets_list_json'),
    path('spreadsheets/', views.display_spreadsheets, name='display_spreadsheets'),

    path('spreadsheets-list-json/<str:spreadsheet_id>/', views.get_spreadsheets_data_json, name='get_spreadsheets_data_json'),
    path('spreadsheets/<str:spreadsheet_id>/', views.display_spreadsheet_data, name='display_spreadsheet_data'),


]
