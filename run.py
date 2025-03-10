import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('nexuscare')

user = SHEET.worksheet('user')
home = SHEET.worksheet('home')
medication = SHEET.worksheet('medication')
schedule = SHEET.worksheet('schedule')


def user_name():
    """
    Enter and log user name
    """


name = input('Please enter your name here: ')
print(f'Hello {name}')

user_name()