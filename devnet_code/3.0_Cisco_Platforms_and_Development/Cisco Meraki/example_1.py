"""
This Example Focuses on Cisco Meraki via the sandbox at
https://devnetsandbox.cisco.com/RM/Diagram/Index/f381be67-d43c-4fc7-977d-0979b04d64cd
Objective:
    Utilize the platform via the requests module
"""

import pprint
import requests
import time

base_url = "https://api.meraki.com/api/v0"
auth_token = "02a3afda271cb9f7106265011bb49f216880332c"
headers = {"X-Cisco-Meraki-API-Key": auth_token}


def get_uri(locator):
    return str(base_url+locator)


def get_data(uri):
    response = requests.get(uri, headers=headers)
    return response


def get_org():
    uri = get_uri("/organizations")
    data = get_data(uri)
    return data.json()


def get_networks(org_id):
    uri = get_uri(f'/organizations/{org_id}/networks')
    data = get_data(uri)
    return data.json()


def get_network_devices(org_id, networks, network_name):
    data = networks
    for values in data:
        if values['name'] == network_name:
            uri = get_uri(f'/organizations/{org_id}/networks/{values["id"]}/devices')
            network_devices = get_data(uri)
            return network_devices
    return


def main():
    org = get_org()
    print(org)
    time.sleep(1)
    org_id = org[0]['id']
    all_networks = get_networks(org_id)
    time.sleep(1)
    org_network_devices = get_network_devices(org_id, all_networks, 'DNSMB3-fxxxxxx1gmail.com')
    print(
        f'Organization ID: {org_id}\n'
        f'Raw Response (Networks): {all_networks}\n'
        f'Network Devices For Organization {org_id}:\n'
    )
    for values in org_network_devices.json():
        print(
            f'Address: {values["address"]}\n'
            f'Firmware: {values["firmware"]}\n'
            f'Floor Plan ID: {values["floorPlanId"]}\n'
            f'Lan IP: {values["lanIp"]}\n'
            f'Latitude: {values["lat"]}\n'
            f'Longitude: {values["lng"]}\n'
            f'MAC: {values["mac"]}\n'
            f'Model: {values["model"]}\n'
            f'Network ID: {values["networkId"]}\n'
            f'Serial: {values["serial"]}\n'
            f'URL: {values["url"]}\n'
        )
    return


def get_all_networks():
    org = get_org()
    print(org)
    if org == "{'errors': ['API rate limit exceeded for organization']}":
        print(org)
    else:
        org_id = org[0]['id']
        all_networks = get_networks(org_id)
        for value in all_networks:
            print(f'Network ID: {value["id"]}\n'
                  f'Network Name: {value["name"]}\n')
            uri = get_uri(f'/organizations/{org_id}/networks/{value["id"]}/devices')
            network_devices = get_data(uri)
            for values in network_devices.json():
                print(
                    f'Address: {values["address"]}\n'
                    f'Firmware: {values["firmware"]}\n'
                    f'Floor Plan ID: {values["floorPlanId"]}\n'
                    f'Lan IP: {values["lanIp"]}\n'
                    f'Latitude: {values["lat"]}\n'
                    f'Longitude: {values["lng"]}\n'
                    f'MAC: {values["mac"]}\n'
                    f'Model: {values["model"]}\n'
                    f'Network ID: {values["networkId"]}\n'
                    f'Serial: {values["serial"]}\n'
                    f'URL: {values["url"]}\n'
                )
                time.sleep(2)

    return


if __name__ == '__main__':
    main()
