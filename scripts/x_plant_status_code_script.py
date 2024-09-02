import pandas as pd
import json

def excel_to_json(path_to_excel, sheet_name='Sheet1'):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name)

    df.columns = ['speed_item_description', 's4_material_description', 's4_material_staus_code', 'comments']

    data = df.to_dict('records')

    json_data = json.dumps(data, indent=4)

    return json_data

excel_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\x_plant_status_code_xref.xlsx"
json_op = excel_to_json(excel_path)
print(json_op)

with open('x_plant_status_code.json', 'w') as json_1:
    json_1.write(json_op)