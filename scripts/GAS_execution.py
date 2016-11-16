import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from apiclient import errors

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import json

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/script-python-quickstart.json
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Python-GAS Spreadsheet Data Script'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'script-python-quickstart.json')

    store = Storage(credential_path)

#use if you want to store credentials locally
    # credentials = store.get()
    # if not credentials or credentials.invalid:
    #     flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    #     flow.user_agent = APPLICATION_NAME
    #     if flags:
    #         credentials = tools.run_flow(flow, store, flags)
    #     else: # Needed only for compatibility with Python 2.6
    #         credentials = tools.run(flow, store)
    #     print('Storing credentials to ' + credential_path)
    # return credentials


    ### no need to store everytime if we're not making too many calls
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
        credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
        credentials = tools.run(flow, store)
    return credentials

def get_spreadsheet_data():
    """Makes a call to the GAS script to get SS data

    Takes in a parameter that denotes the specific type of parameter
    """
    SCRIPT_ID = '11haDlAIieNhugt6puckZJ1Js1XoXCCrgz8WcRzzzskgodfiDDjmLss1J'

    # Authorize and create a service object.
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('script', 'v1', http=http)

    # Create an execution request object.
    request = {"function": "getGeoData"}

    try:
        # Make the API request.
        response = service.scripts().run(body=request,
                scriptId=SCRIPT_ID).execute()

        if 'error' in response:
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                        trace['lineNumber']))
        else:
            circ_response = response['response'].get('result', {})
            if not circ_response:
                print('No data returned')
            else:
                return json.loads(circ_response)

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print(e.content)



if __name__ == '__main__':
    circ_response = get_spreadsheet_data()
    headers = circ_response['headers']
    circ_data = circ_response['data']

    print circ_data
