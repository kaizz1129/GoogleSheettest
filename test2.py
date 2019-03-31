#%%
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES= ['https://www.googleapis.com/auth/spreadsheet']
creds = None
if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheets = service.spreadsheets()

print("complete connect API")

spreadsheet_id='1cPRgbGB5jPIypHfcr9K9APfQIRdppa7R7530AsRqyCE'
range_ = 'DATA!A1:E1'

#不處理直接填入
value_input_option = 'RAW'
#插入在新欄位 
insert_data_option = 'INSERT_ROWS'

_body={
  "range": 'DATA!A1:E1',
  "majorDimension": "ROWS",
  "values": [
    ["Door", "$15", "2", "3/15/2016"],
    ["Engine", "$100", "1", "3/20/2016"],
  ],
}

request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=_body)
response = request.execute()
print(response)


#%%
