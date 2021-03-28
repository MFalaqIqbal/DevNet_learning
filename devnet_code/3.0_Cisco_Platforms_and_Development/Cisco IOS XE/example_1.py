from device_info import ios_xe1
from ncclient import manager
from xml.dom.minidom import parseString, parse
from jinja2 import Template
import xmltodict
import pprint


def init_connection():
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as connection:
        return connection


def get_int_details(connection, interface):
    xml = f"""
            <filter>
              <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                  <name>{interface}</name>
                </interface>
              </interfaces>
              <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                  <name>{interface}</name>
                </interface>
              </interfaces-state>
            </filter>
            """
    data = connection.get(xml)
    data_parsed = xmltodict.parse(data.xml)["rpc-reply"]["data"]
    int_config = data_parsed["interfaces"]["interface"]
    int_stats = data_parsed["interfaces-state"]["interface"]
    # pprint.pprint(int_config)
    # pprint.pprint(int_stats)
    print('-' * 50)
    print(
        f'Interface Details:\n'
        f'Name: {int_config["name"]["#text"]}\n'
        f'Description: {int_config["description"]}\n'
        f'Type: {int_config["type"]["#text"]}\n'
        f'MAC: {int_stats["phys-address"]}\n'
        f'Speed: {int_stats["speed"]}\n'
        f'Statistics:\n'
        f'\t Discontinuity-Time: {int_stats["statistics"]["discontinuity-time"]}'
    )
    print('-' * 50)
    return


def push_int_details(connection, payload):
    _payload = Template(payload)
    rendered = _payload.render(
        DESCRIPTION="WandaVision"
    )
    result = connection.edit_config(target='running', config=rendered)
    return


def main():

    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as connection:
        # get_int_details(connection, "GigabitEthernet2")
        payload = """
                    <config>
                    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                    <name>GigabitEthernet3</name>
                    <description>{{ DESCRIPTION }}</description>
                    </interface>
                    </interfaces>
                    </config>    
                """
        push_int_details(connection, payload)
        get_int_details(connection, "GigabitEthernet3")
    return


if __name__ == '__main__':
    main()
