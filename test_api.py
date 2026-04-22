import requests

endpoint = "/predict"
response = requests.get(f"http://localhost:8000{endpoint}")

# The .json() method returns the JSON response as a Python dictionary
data = response.json()

print(data)