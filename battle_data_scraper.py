import json
import requests
import os

for i in range(1, 100):
    file = f'./data/battle_ids/battle_ids_{i}.json'

    with open(file, 'r') as f:
        data = json.load(f)

        for game in data:
            id = game["id"]
            url = f'https://replay.pokemonshowdown.com/{id}.json'
            replay_file = f'./data/battle_data/{id}.json'

            # Only proceed if the file doesn't already exist
            if not os.path.exists(replay_file):
                response = requests.get(url)

                if response.status_code == 200:
                    replay_data = response.json()
                    with open(replay_file, 'w') as rf:
                        json.dump(replay_data, rf)
                    print(f"Saved replay data for battle ID {id} to {replay_file}")
                else:
                    print(f"Failed to retrieve replay data for battle ID {id}: {response.status_code}")
            else:
                continue