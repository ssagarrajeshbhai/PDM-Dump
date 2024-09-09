import pandas as pd

csv_path = r"C:\Users\ssagarrajeshbhai\PycharmProjects\PDM-Dump\src\request_data.csv"
df = pd.read_csv(csv_path)

transaction_id_list = df['transaction_id'].tolist()
material_type = ''
success_flag = ['True', 'False']
error_id = ''

print(transaction_id_list)