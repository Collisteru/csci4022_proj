import json
import requests

url = f'https://pokeapi.co/api/v2/pokemon/ditto'
file = f'./data/pokemon.json'

print("Initialized... getting url...")
response = requests.get(url)
print("Line 8")
if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")

    with open(file, 'w') as rf:
        json.dump(data, rf)
    print(f"Saved replay data for battle ID {id} to {file}")
else:
    print(f"Failed to retrieve data: {response.status_code}")