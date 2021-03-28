"""
This Example Focuses on Cisco Meraki via the sandbox at
https://devnetsandbox.cisco.com/RM/Diagram/Index/f381be67-d43c-4fc7-977d-0979b04d64cd
Objective:
    Utilize the platform via the meraki sdk
"""

import meraki
import json
from pprint import pprint

auth_token = "02a3afda271cb9f7106265011bb49f216880332c"

dashboard_api = meraki.DashboardAPI(auth_token)


def get_org_list():
    organizations = dashboard_api.organizations.getOrganizations()
    return organizations


def get_org_networks(org_id):
    org_networks = dashboard_api.organizations.getOrganizationNetworks(organizationId=org_id)
    return org_networks


def get_network_devices(network_id):
    net_devs = dashboard_api.networks.getNetworkDevices(network_id)
    return net_devs


def display_all_devices(networks):
    for value in networks:
        print(f'value["name]\n')
        devices = get_network_devices(value['id'])
        pprint(devices)
    return


def update_net(net_id, name):
    update = dashboard_api.networks.updateNetwork(networkId=net_id, name=name)
    return update


def update_net_dev(net_id, serial):
    update = dashboard_api.devices.updateDevice(
        'Q2HP-Q9S8-BVHB',
        name="SWITCH_12_28",
        tags=['Test1', 'Test2']
    )
    return update


def get_device_lldp_cdp(serial):
    data = dashboard_api.devices.getDeviceLldpCdp(serial=serial)
    pprint(data)
    return


def main():
    org_id = get_org_list()[0]['id']
    org_networks = get_org_networks(org_id)
    update_net_dev(None, None)
    for value in org_networks:
        if value['name'] == 'TheBoys':
            devices = get_network_devices(value['id'])
            # update_net(value['id'], "TheBoys")
            # update_net_dev(value['id'], value['serial'])
            pprint(devices)
    return


if __name__ == '__main__':
    main()
