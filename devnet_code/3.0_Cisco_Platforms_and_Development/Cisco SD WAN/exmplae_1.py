import requests
import json
import urllib3
from pprint import pprint, PrettyPrinter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandbox-sdwan-1.cisco.com:443/"
username = "devnetuser"
password = "RG!_Yw919_83"
login_url = base_url + "j_security_check"
header = {'Content-Type': 'application/x-www-form-urlencoded'}
login_data = {'j_username': username, 'j_password': password}


def connection_setup():
    session = requests.session()
    login = session.post(url=login_url, data=login_data, verify=False)
    login_token = session.get(url=base_url+"dataservice/client/token", verify=False)
    session.headers['X-XSRF-TOKEN'] = login_token.content
    return session


def get_login_token(session):
    login_token = session.get(url=base_url+"dataservice/client/token", verify=False)
    return login_token.content


def get_device_list(session):
    request = session.get(url=base_url+"dataservice/device", verify=False)
    return request.json()


def main():
    SESSION = connection_setup()
    DEVICE_LIST = get_device_list(SESSION)
    for dev in DEVICE_LIST["data"]:
        print(f'Device IP --> {dev["system-ip"]:<12} Name: {dev["host-name"]}')
    SYSTEM_DEVICE = SESSION.get(url=base_url+"dataservice/statistics/bridgeinterface", verify=False)
    pprint(SYSTEM_DEVICE.json())
    return


if __name__ == "__main__":
    main()
