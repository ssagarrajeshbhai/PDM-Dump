from dummy_request_data import transaction_id_list, material_type_list, success_flag, error_id_list
import random, json

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


def generate_sample_data(count):
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
            trans["succes_payload"] = trans["incoming_payload"]
            trans["error_id"] = None
            trans["event_status_message"] = "Success"
        else:
            trans["succes_payload"] = None
            trans["error_id"] = f'{random.choice(error_id_list)}'
            trans["event_status_message"] = "Failed"

        final_json.append(trans)

    return json.dumps(final_json, indent=3)

count = 1
j_data = generate_sample_data(count)
file_name = f'data{count}.json'
with open(file_name, 'w') as json_writer:
    json_writer.write(j_data)