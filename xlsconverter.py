import pandas as pd

def convert_csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Write JSON data to file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

# Example usage:
csv_file_path = 'K-Felder_Definition_FeP_neu.csv'
json_file_path = 'output_file.json'
convert_csv_to_json(csv_file_path, json_file_path)
