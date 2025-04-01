import json
import requests

for i in range(1,100):
    url = f'https://replay.pokemonshowdown.com/search.json?format=[Gen%209]%20VGC%202025%20Reg%20G%20(Bo3&page={i}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(f'./data/battle_ids_{i}.json', 'w') as f:
            json.dump(data, f)
    else:
        print(f"Failed to retrieve data: {response.status_code}")