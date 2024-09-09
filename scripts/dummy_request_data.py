import pandas as pd

transaction_id_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\request_data.csv"
material_type_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\material_type_data.csv"
error_id_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\dummy_error_data.csv"

transaction_id_df = pd.read_csv(transaction_id_path)
material_type_df = pd.read_csv(material_type_path)
error_id_df = pd.read_csv(error_id_path)

transaction_id_list = transaction_id_df['transaction_id'].tolist()
material_type_list = material_type_df['id'].tolist()
success_flag = ['True', 'False']
error_id_list = error_id_df['id'].tolist()

print(transaction_id_list)
print(material_type_list)
print(error_id_list)