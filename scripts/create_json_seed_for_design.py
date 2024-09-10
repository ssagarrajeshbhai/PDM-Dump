from dummy_request_data import transaction_id_list,error_report_id_list, material_type_list, payload_id_list, success_flag, error_id_list
import random, json

op_payload_id = "b8b176c4-a0e7-4874-a32d-363f01f6c8ce"
def generate_sample_data():
    final_json = []
    # for i in range(50):

    for t_id in range(1000):
        trans = {
            "transaction_id": transaction_id_list[t_id%len(transaction_id_list)],
            "material_type": random.choice(material_type_list),
            "mmid": f'mmid{t_id + 1}',
            "incoming_payload": random.choice(payload_id_list),
            "success_flag": random.choice(success_flag)
        }

        if trans["success_flag"]:
            trans["succes_payload"] = op_payload_id
            trans["error_id"] = None
            trans["event_status_message"] = "Success"
        else:
            trans["success_payload"] = None
            trans["error_id"] = f'{random.choice(error_report_id_list)}'
            trans["event_status_message"] = "Failed"

        final_json.append(trans)

    return json.dumps(final_json, indent=3)

j_data = generate_sample_data()
file_name = f'design2.json'
with open(file_name, 'w') as json_writer:
    json_writer.write(j_data)