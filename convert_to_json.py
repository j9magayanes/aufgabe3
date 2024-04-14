# import pandas as pd

# def convert_xls_to_json(xls_file_path, json_file_path):
#     df = pd.read_excel(xls_file_path)

#     json_data = df.to_json(orient='records')

#     with open(json_file_path, 'w') as json_file:
#         json_file.write(json_data)

# xls_file_path = 'K-Felder_Definition_FeP_neu.xls'
# json_file_path = 'output_file.json'
# convert_xls_to_json(xls_file_path, json_file_path)

import pandas
import json

excel_data_df = pandas.read_excel('K-Felder_Definition_FeP_neu.xls', sheet_name='K-Feldliste')

thisisjson = excel_data_df.to_json(orient='records')


print('Excel Sheet to JSON:\n', thisisjson)

thisisjson_dict = json.loads(thisisjson)


with open('data.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)
