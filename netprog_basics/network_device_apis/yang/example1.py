#! /usr/bin/env python
"""
example1.py
Illustrate the following concepts:
- Connect with NETCONF
- Print to screen the <data>
- Used to compare to data model
"""

from device_info import ios_xe1
from ncclient import manager
import xml.dom.minidom
import xmltodict

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()
second = open("filter-ietf-ip.xml").read()


def get_info_model(connection, get_type, filter):
    if get_type == 1:
        _reply = connection.get_config("running", filter)
        data = xml.dom.minidom.parseString(_reply.xml)
        return data
    else:
        _reply = connection.get_config("running")
        data = xml.dom.minidom.parseString(_reply.xml)
        return data


if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        info = get_info_model(m, 0, None)
        get_xml_interfaces_data = info.getElementsByTagName("interfaces")
        print(get_xml_interfaces_data[0].toprettyxml())
        print('-' * 50)
        info = get_info_model(m, 1, netconf_filter)
        get_info_via_model = info.getElementsByTagName("interfaces")
        print(get_info_via_model[0].toprettyxml())
        print('-' * 50)
        # print YANG module
        print('***Saving the YANG Module***')
        data = m.get_schema('ietf-interfaces')
        xml_doc = xml.dom.minidom.parseString(data.xml)
        yang_module = xml_doc.getElementsByTagName("data")
        print(yang_module[0].toprettyxml())

        # print(type(interfaces))
        # print(interfaces[1].toprettyxml())
        # for vlu in interfaces:
        #     print(vlu.toprettyxml())
