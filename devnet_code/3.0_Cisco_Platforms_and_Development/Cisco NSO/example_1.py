import requests
from pprint import pprint

username = "developer"
password = "BallGreenFoot23!"

base_url = "https://devasc-nso-1.cisco.com/restconf/data/tailf-ncs:"


def get_data(url):
    head = {
        "Content-Type": "application/yang-data+json"
    }
    req = requests.get(url,
                       auth=(username, password),
                       headers=head,
                       verify=False)
    return req


def main():
    GET_DEVICES_URL = base_url + "devices/device=ios0/config"
    GET_DEVICES = get_data(GET_DEVICES_URL)
    print(GET_DEVICES.text)
    print('-' * 100)
    GET_SERVICES_URL = base_url + "services/"
    GET_SERVICES = get_data(GET_SERVICES_URL)
    print(GET_SERVICES.text)
    print('-' * 100)
    GET_LOOPBACK_URL = base_url + "services/loopbackdevnet:loopbackdevnet=tpl1"
    GET_LOOPBACK = get_data(GET_LOOPBACK_URL)
    print(GET_LOOPBACK.text)
    return


if __name__ == "__main__":
    main()