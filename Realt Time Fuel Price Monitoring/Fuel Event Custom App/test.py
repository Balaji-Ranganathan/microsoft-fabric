
import json
import requests
import uuid
import calendar
import time
from datetime import datetime, timedelta
from time import mktime

# Getting the current date and time
#dt = datetime.now()
current_GMT = time.gmtime()
dt = datetime.fromtimestamp(mktime(current_GMT)) 
# getting the timestamp
ts = datetime.timestamp(dt)
# convert to datetime
#date_time = datetime.fromtimestamp(ts)
# convert timestamp to string in dd-mm-yyyy HH:MM:SS
str_date_time = dt.strftime("%d/%m/%Y, %H:%M:%S %p")
date_time_from = dt - timedelta(days=1)
str_date_time_from = date_time_from.strftime("%d/%m/%Y, %H:%M:%S %p")

transactionid = str(uuid.uuid4())

url = "https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken"

querystring = {"grant_type":"client_credentials"}

headers = {
    'content-type': "application/json",
    'authorization': "Basic UGJLWXROZmZSdUZWdWloS1VPaERZanM2R21CellYY0E6OXdBc1FmdFJlMWtpVHZ3RA=="
    }

response_text = requests.request("GET", url, headers=headers, params=querystring)

print(response_text.text)


# Parse the JSON response
response_json = json.loads(response_text.text)

# Access the value of "refresh_token_expires_in"
refresh_token_expires_in = response_json.get("refresh_token_expires_in")
access_token = response_json.get("access_token")
client_id = response_json.get("client_id")
# Print the value
print("refresh_token_expires_in:", refresh_token_expires_in)



url_lovs_ = "https://api.onegov.nsw.gov.au/FuelCheckRefData/v1/fuel/lovs"
querystring = {"states":""}
# request timezone UTC date and time of request. Format dd/MM/yyyy hh:mm:ss AM/PM

headers = {
    'content-type': "application/json",
    'authorization': "Bearer "+access_token,
    'client_id': client_id,
    'transactionid': transactionid,
    'requesttimestamp': str_date_time,
    'if-modified-since': str_date_time_from
    }

response_lovs = requests.request("GET", url, headers=headers, params=querystring)

print("this is response lovs",response_lovs.text)
print("so far ok")

#
#'apikey': client_id,