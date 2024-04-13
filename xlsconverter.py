# import pandas as pd

# def convert_xls_to_json(xls_file_path, json_file_path):
#     # Read the Excel file into a pandas DataFrame
#     df = pd.read_excel(xls_file_path)

#     # Convert DataFrame to JSON
#     json_data = df.to_json(orient='records')

#     # Write JSON data to file
#     with open(json_file_path, 'w') as json_file:
#         json_file.write(json_data)

# # Example usage:
# xls_file_path = 'K-Felder_Definition_FeP_neu.xls'
# json_file_path = 'output_file.json'
# convert_xls_to_json(xls_file_path, json_file_path)

import pandas
import json

# Read excel document
excel_data_df = pandas.read_excel('K-Felder_Definition_FeP_neu.xls', sheet_name='K-Feldliste')

# Convert excel to string 
# (define orientation of document in this case from up to down)
thisisjson = excel_data_df.to_json(orient='records')

# Print out the result
print('Excel Sheet to JSON:\n', thisisjson)

# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)

# Define file to write to and 'w' for write option -> json.dump() 
# defining the list to write from and file to write to
with open('data.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)
