import csv
import requests

# Function to read data from a CSV file
def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to write data to a CSV file
def write_csv(data, file_path):
    if data:
        keys = data[0].keys()
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

# Function to integrate data with an API
def integrate_with_api(data, api_url):
    headers = {'Content-Type': 'application/json'}
    for item in data:
        response = requests.post(api_url, json=item, headers=headers)
        if response.status_code != 201:
            print(f"Failed to integrate {item}: {response.text}")

# Example usage
csv_file_path = 'data.csv'
api_url = 'https://example.com/api/data'

# Read data from CSV
data = read_csv(csv_file_path)

# Integrate data with API
integrate_with_api(data, api_url)

# Optionally, write updated data back to CSV
write_csv(data, csv_file_path)