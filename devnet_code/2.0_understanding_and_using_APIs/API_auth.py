
import requests
from requests.auth import HTTPBasicAuth
import json
import sys
# Here we will attempt to retrieve all user accounts from the library
# Since user accounts are considered a protected resource, only those who have
# admin credentials should be able to access it.
url = "http://localhost:8080/v1/accounts"

## This is unsafe as the username and password are stored in plain text
username = 'admin'
password = 'w0FimhVrty1ck9Pf2UAK4luOnkEgrDvy1VEK9iZsZOk='

# Leverage the HTTPBasicAuth class provided by the requests package
accounts = requests.get(url, auth=HTTPBasicAuth(username, password))
try:
    accounts.raise_for_status()
except requests.exceptions.HTTPError as e:
    # this code will not be executed if the username and password are correct!
    print("Error: {}".format(e))
    sys.exit()
# This code will be executed
print(accounts.status_code)

import requests
from requests.auth import HTTPBasicAuth
import json
import sys
# Here we will attempt to retrieve all user accounts from the library
# Since user accounts are considered a protected resource, only those who have
# admin credentials should be able to access it.
url = "http://localhost:8080/v1/accounts"

## This is unsafe as the username and password are stored in plain text
username = 'admin'
password = 'w0FimhVrty1ck9Pf2UAK4luOnkEgrDvy1VEK9iZsZOk='

# Leverage the HTTPBasicAuth class provided by the requests package
accounts = requests.get(url, auth=HTTPBasicAuth(username, password))
try:
    accounts.raise_for_status()
except requests.exceptions.HTTPError as e:
    # this code will not be executed if the username and password are correct!
    print("Error: {}".format(e))
    sys.exit()
# This code will be executed
print(accounts.status_code)
