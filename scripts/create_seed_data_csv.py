import pandas as pd
from dummy_request_data import transaction_id_list, material_type_list, success_flag, error_id_list
import random, json

csv_file_path = 'data.csv'
columns = ['transaction_id', 'material_type', 'mmid', 'incoming_payload', 'success_flag', 'succes_payload', 'error_id', 'event_status_message']

payload_obj = {
    "transactionId": "123e4567e89b12d3a456426614174000",
    "item": {
        "basicData": {
            "materialNumber": "",
            "materialType": "",
            "materialGroup": "",
            "grossWeight": 2.3,
            "transportationGroup": 3,
            "netWeight": 3,
            "crossPlantStatusCode": 12,
            "division": 1,
            "waferConductivityType": "sdf",
            "waferSpecialIdCode": "12344s",
            "waferSequenceCode": "aas2",
            "supplierCode": "23gg"
        },
        "classificationData": {
            "characteristicName": "",
            "characteristicValue": "a",
            "class": "",
            "classType": 4
        },
        "hierarchyLinkData": {
            "forecastClass": "",
            "forecastDevice": "",
            "forecastPackage": ""
        },
        "materialLongText": {
            "lineNumber": 12345,
            "applicationObject": "",
            "textName": "",
            "textId": 1244
        }
    }
}

success_payload_obj = {
  "success": "true",
  "code": "201 - SUCCESS",
  "data": {
    "transactionId": "123e4567e89b12d3a456426614174000",
    "item": {
      "basicData": {
        "materialType": "HALB",
        "materialNumber": "NNNN-NNNN",
        "alternateNumber": "H90226-001"
      }
    }
  }
}


def generate_sample_data():
    final_json = []
    # for i in range(50):

    for t_id in range(20):
        trans = {
            "transaction_id": transaction_id_list[t_id],
            "material_type": random.choice(material_type_list),
            "mmid": f'mmid{t_id + 1}',
            "incoming_payload": payload_obj,
            "success_flag": random.choice(success_flag)
        }

        if trans["success_flag"]:
            trans["succes_payload"] = success_payload_obj
            trans["error_id"] = None
            trans["event_status_message"] = "Success"
        else:
            trans["succes_payload"] = None
            trans["error_id"] = f'{random.choice(error_id_list)}'
            trans["event_status_message"] = "Failed"


        final_json.append(trans)
        json_df = pd.DataFrame([trans])

        ## append the df to the csv file
        json_df.to_csv(csv_file_path, mode = 'a', header=True, index=False)

    print(final_json)

a = generate_sample_data()