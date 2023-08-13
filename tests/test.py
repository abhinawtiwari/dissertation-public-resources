import csv
import json

def csv_to_json(csv_file, json_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        data = list(csv_data)

    # Write the JSON data to a file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Provide the paths to the CSV and JSON files
csv_file_path = './temp_diss.csv'
json_file_path = './temp_diss_output.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)
