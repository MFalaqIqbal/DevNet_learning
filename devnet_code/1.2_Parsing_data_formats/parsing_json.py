import json
from pprint import pprint

with open("D:\\DevNet\\DevNet\\devnet_code\\1.2_Parsing_data_formats\\address_list.json") as f:
    json_dic = json.load(f)
pprint(json_dic)

print("")

str_dic = """ {"Key_1": "value_1", "Key_2": "value_2", "Key_3": "value_3"} """
json_dic = json.loads(str_dic)
pprint(json_dic)

with open("D:\\DevNet\\DevNet\\devnet_code\\1.2_Parsing_data_formats\\test.json", "w") as f:
    json.dump(json_dic, f,sort_keys=True, indent = 4, ensure_ascii=False)  # Presents the data in proper json format
   
