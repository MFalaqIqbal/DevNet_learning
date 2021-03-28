import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

base_url = "https://sandboxapicdc.cisco.com/"
base_url_2 = "https://devasc-aci-1.cisco.com/"
base_url_3 = "https://devasc-aci-2.cisco.com/"


def apic_login():
    payload = {
            "aaaUser": {
                "attributes": {
                    "name": "devnetuser",
                    "pwd": "CardBoardGreen12!"
                }
            }
        }
    head = {"Content-Type": "application/json; charset=utf-8"}
    req = requests.post(
        url=base_url_2+"api/aaaLogin.json",
        headers=head,
        data=json.dumps(payload),
        verify=False
    ).json()
    token = req["imdata"][0]['aaaLogin']['attributes']['token']
    return token


def get_data(token, url):
    req = requests.get(
        url=url,
        headers={
            "Cookie": f"APIC-cookie={token}",
            "Content-Type": "application/json; charset=utf-8"},
        verify=False)
    return req


def main():
    TOKEN = apic_login()
    GET_TENANTS = get_data(TOKEN, f'{base_url_2}api/node/class/fvTenant.json')
    GET_DEVICES = get_data(TOKEN, f'{base_url_2}api/node/class/topology/pod-1/topSystem.json')
    print('-' * 10, "All Tenants", '-' * 10)
    pprint(GET_TENANTS.json())
    print('-' * 10, "Devices", '-' * 10)
    pprint(GET_DEVICES.json())
    return


if __name__ == "__main__":
    main()
