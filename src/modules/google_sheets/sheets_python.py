"""
    Module to facilitate interaction
    with Google Sheets
"""

# ---------------- BASE PYTHON LIBS ----------------◹
from __future__ import print_function
import os
# --------------------------------------------------◿

# -------------------- IMPORTED LIBS -------------------◹
from pandas import DataFrame
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials, exceptions
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# from googleapiclient.errors import HttpError
# ------------------------------------------------------◿

class SheetsPython:
    """
        Class with functions necessary for Python
        to communicate with Google Sheets
    """
    def __init__(self) -> None:
        self.token_path : str = os.path.join(os.getcwd(),
                                             'assets\\token.json')
        self.credential_path : str = os.path.join(os.getcwd(),
                                                  'assets\\credentials.json')
        self.scopes : list[str] = [
            'https://www.googleapis.com/auth/spreadsheets']
        self.creds : Credentials | None = None

    def __verify_creeds(self) -> None:
        """
            Function with the aim of facilitating the creation
            of Google credentials, Google's standard way
            of validating dates is quite boring,
            so I set up this "While True" with "os" to edit
            the files during the attempt
        """
        while True:
            try:
                if os.path.exists(self.token_path):
                    self.creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)
                if not self.creds or not self.creds.valid:
                    if self.creds and self.creds.expired and self.creds.refresh_token:
                        self.creds.refresh(Request())
                    else:
                        flow : InstalledAppFlow = InstalledAppFlow.from_client_secrets_file(
                            self.credential_path, self.scopes)
                        self.creds = flow.run_local_server(port=0)
                    with open(self.token_path, 'w', encoding="utf-8") as token:
                        token.write(self.creds.to_json())
                break
            except (FileNotFoundError,exceptions.RefreshError):
                self.creds = None
                if os.path.exists(self.token_path):
                    os.remove(self.token_path)

    def get_data_from_sheets(self,
                             id_sheets : str,
                             range_sheets : str,
                             with_headers : bool = True) -> DataFrame:
        """
            As the name says, this function get data from
            given SpreadSheets

        Args:
            id_sheets (str): SpreadSheets Id
            range_sheets (str): SpreadSheets Range
            with_headers (bool, optional): Consider the first line as the header?. Defaults to True.

        Returns:
            DataFrame: Extracted infos as a DataFrame
        """
        self.__verify_creeds()

        service = build(serviceName='sheets',
                        version='v4',
                        credentials=self.creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id_sheets,
                                    range=range_sheets).execute()

        values = result.get('values', [])
        if with_headers:
            if len(values[0]) > len(values[1]):
                for row in values[1:]:
                    while len(row) < len(values[0]):
                        row.append("")
            values_as_df = DataFrame(values[1:],columns=values[0])
        else:
            values_as_df = DataFrame(values)

        if values_as_df.empty:
            print('\033[41m\033[30m'
                  'Careful! The sheet query was successful, but the data came up empty'
                  '\033[0m\033[0m')

        return values_as_df

    def update_sheets_data(self, data_frame : DataFrame,
                                 id_sheets : str,
                                 range_sheets : str,
                                 clear : bool = False,
                                 range_clear : str | None = None,
                                 append : bool = False,
                                 append_col_ref : str | None = None) -> None:

        """As the name suggests, this function updates
        data from a Google Sheets spreadsheet"""

        data_frame = data_frame.fillna('')
        data_list = data_frame.values.tolist()

        if not data_list:
            raise ValueError('The given DataFrame is empty')

        self.__verify_creeds()

        service = build(serviceName='sheets',
                        version='v4',
                        credentials=self.creds)
        sheet = service.spreadsheets()
        if append and append_col_ref is not None:
            range_aux = range_sheets.split('!')
            range_ref = range_aux[0]
            range_ref = f"{range_ref}!{append_col_ref}1:{append_col_ref}"
            data_from_ref_col = self.get_data_from_sheets(id_sheets=id_sheets, range_sheets=range_ref,with_headers=False)
            last_row = len(data_from_ref_col) + 1
            range_aux2 = range_aux[1].split(':')
            new_sheets_range = f"{range_aux[0]}!{range_aux2[0]}{last_row}:{range_aux2[1]}"
            range_sheets = new_sheets_range

        if clear and range_clear is not None:
            sheet.values().clear(spreadsheetId=id_sheets,
                                        range=range_clear).execute()

        print(f'Updating Google Sheets with range: {range_sheets}')
        sheet.values().update(spreadsheetId = id_sheets,
                            range= range_sheets, valueInputOption = 'USER_ENTERED',
                            body = {"values": data_list}).execute()
