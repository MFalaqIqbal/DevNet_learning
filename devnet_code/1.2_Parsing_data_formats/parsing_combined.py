import json
import yaml
import xmltodict
from lxml import etree as ET
from pprint import pprint

global locations
locations = "D:\\DevNet\\DevNet\\devnet_code\\1.2_Parsing_data_formats\\"

def json_load():
    global locations
    loc = locations + "address_list.json"
    with open(loc) as file:
        data = json.load(file)
    file.close()
    pprint(data)
    return
  
def xml_load():
    global locations
    loc = locations + "address_list.xml"
    with open(loc) as file:
        data = ET.parse(file)
        roots = data.getroot()
        for root in roots:
            print(ET.tostring(root), root.get("Id"))
    return

def xml_xmltodict():
    global locations
    loc = locations + "address_list.xml"
    with open(loc) as file:
        data = xmltodict.parse(file.read())
        pprint(data)
        print("")
        for stuff in data['root']['addresses']:
            print(stuff)
    return
    
def yaml_load():
    global locations
    loc = locations + "address_list.yaml"
    with open(loc) as file:
        data = yaml.safe_load(file)
        pprint(data)
    return
    
if __name__ == "__main__":
    print("Json:")
    json_load()
    print("XML ETree Load:")
    xml_load()
    print("XML to Dict:")
    xml_xmltodict()
    print("Yaml:")
    yaml_load()
    