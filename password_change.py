import csv
import getpass
import requests
from requests.auth import HTTPBasicAuth

# Ask the user for the location of the CSV file containing Isilon cluster information
csv_file = input("Enter the location of the CSV file containing Isilon cluster information: ")

# Ask the user for the old and new root passwords (hidden input)
old_password = getpass.getpass(prompt="Enter the old root password: ")
new_password = getpass.getpass(prompt="Enter the new root password: ")

# Set the OnFS API endpoint and version
onfs_endpoint = "/platform/3"
onfs_version = "8.2.2.0"

# Read the FQDNs from the CSV file
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    fqdns = [row[0] for row in reader]

# Loop through each FQDN and change the root password
for fqdn in fqdns:
    # Construct the OnFS API URL for changing the root password
    url = f"https://{fqdn}:8080{onfs_endpoint}/auth/change_password"

    # Set the headers and data for changing the root password
    headers = {"Content-Type": "application/json"}
    data = {"old_password": old_password, "new_password": new_password}

    # Send a PUT request to change the root password with HTTP basic authentication
    response = requests.put(url, auth=HTTPBasicAuth("root", old_password), headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Changed root password on {fqdn}.")
    else:
        print(f"Failed to change root password on {fqdn}.")
