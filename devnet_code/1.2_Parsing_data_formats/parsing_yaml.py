import yaml

with open("D:\\DevNet\\DevNet\\devnet_code\\1.2_Parsing_data_formats\\address_list.yaml") as f:
    yaml_dic = yaml.safe_load(f)

with open("test.yaml", "w") as f:
    yaml.dump(yaml_dic, f)

print(yaml_dic)