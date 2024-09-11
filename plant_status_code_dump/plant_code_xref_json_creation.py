import pandas as pd
import json

def excel_to_json(path_to_excel, sheet_name='Sheet1'):
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name)

    df.columns = ['plant_code', 'sap_plant_code', 's4_plant_code', 'observation']

    data = df.to_dict('records')

    json_data = json.dumps(data, indent=4)

    return json_data

excel_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\plant_code_xref.xlsx"
json_op = excel_to_json(excel_path)
print(json_op)

with open('plant_code_xref.json', 'w') as json_1:
    json_1.write(json_op)