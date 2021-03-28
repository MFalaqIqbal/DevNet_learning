import requests
import json
from pprint import pprint

API_KEY = '8f90ecec4fca692f606092279f203c6020ca011c'
base_url = "https://api.meraki.com/api/v0/"


def get_data(url, *args):
    headers = {"X-Cisco-Meraki-API-Key": API_KEY}
    if args == ():
        req = requests.get(url, headers=headers)
    else:
        req = requests.get(url, headers=headers, params=args[0])
    return req


def main():
    GET_ORG_URL = base_url + "organizations"
    GET_ORG = get_data(GET_ORG_URL)
    pprint(GET_ORG.json())
    print('*' * 100)
    GET_ORG_DEVICE_URL = base_url + "organizations/566327653141842188/devices"
    GET_ORG_DEVICE = get_data(GET_ORG_DEVICE_URL)
    pprint(GET_ORG_DEVICE.json())
    print("*" * 100)
    GET_PAGINATION_EXP = get_data(GET_ORG_DEVICE_URL, {"perPage": 3})
    pprint(GET_PAGINATION_EXP.json())
    return


if __name__ == "__main__":
    main()