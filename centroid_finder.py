import json
import os
from statistics import mean



script_directory = os.path.dirname(os.path.abspath(__file__))
battle_summaries_path = os.path.join(script_directory, "battle_summaries.json")
pokemon_stats_path = os.path.join(script_directory, "pokemon_stats.json")
team_centroids_path = os.path.join(script_directory, "team_centroids.json")
# This creates the file if it doesn't already exist,
# or erases its contents if it does exist
open(team_centroids_path, 'w').close()

team_centroids_list = []
with open(battle_summaries_path, 'r') as file_battles:
    data_battles = json.load(file_battles)
    with open(pokemon_stats_path, 'r') as file_stats:
        data_stats = json.load(file_stats)

        for battle in data_battles:
            # This program only creates centroids for winning teams
            winner = 1
            if battle[2]:
                winner = 0
            team = battle[winner]

            stats_lists = [data_stats[key.lower()] for key in team]
            transposed = zip(*stats_lists)
            means = [mean(group) for group in transposed]
            team_centroids_list.append(means)

        file_stats.close()
    file_battles.close()

with open(team_centroids_path, 'w') as file_centroids:
    json.dump(team_centroids_list, file_centroids)
    file_centroids.close()
