


#%%

# import pandas as pd
import requests
import urllib3
import time
import pytz
import datetime as dt

urllib3.disable_warnings()

url='https://localhost:5000/v1/api/iserver/auth/status'
count=0

while True:
    now=dt.datetime.now(pytz.timezone('Australia/Brisbane'))
    
    response = requests.post(url=url, verify=False)
    api_status=response.json()

    count=count+1
    if count>5:
        break   

    print(now)
    print(api_status)
    print(count)

    time.sleep(15)


# %%
