import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

import requests


EVENT_HUB_CONNECTION_STR = "sb://esehaustruqp1sq68og7jqhq.servicebus.windows.net/;SharedAccessKeyName=key_212ef3ed-7563-1241-6de8-965f5b951e69;SharedAccessKey=pGUkmztzwXgPLzImWFNYbfWZLdsvfbZbk+AEhGuJK6s="
EVENT_HUB_NAME =  "es_8dca3434-64c8-44cd-bcea-745ed284d29f"


url = "https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken"

querystring = {"grant_type":"client_credentials"}

headers = {
    'content-type': "application/json",
    'authorization': "Basic UGJLWXROZmZSdUZWdWloS1VPaERZanM2R21CellYY0E6OXdBc1FmdFJlMWtpVHZ3RA=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)



print("so far ok")