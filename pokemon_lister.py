import json
import requests

url = f'https://pokeapi.co/api/v2/pokemon'

print("Initialized... getting url...")
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    data = data['results']
    print(f"Data: {data}")
    print(len(data))
else:
    print(f"Failed to retrieve data: {response.status_code}")