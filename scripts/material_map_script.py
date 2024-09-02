import pandas as pd
import json

def excel_to_json(path_to_excel, sheet_name='Sheet1'):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name)

    df.columns = ['source', 'division', 's_4_material_type', 'material_type']

    data = df.to_dict('records')

    json_data = json.dumps(data, indent=4)

    return json_data

excel_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\material_map_xref.xlsx"
json_op = excel_to_json(excel_path)
print(json_op)

with open('material_map.json', 'w') as json_1:
    json_1.write(json_op)