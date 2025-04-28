import json
import os
from statistics import mean

script_directory = os.path.dirname(os.path.abspath(__file__))
battle_summaries_path = os.path.join(script_directory, "battle_summaries.json")
team_scores_path = os.path.join(script_directory, "team_scores.json")
pokemon_stats_path = os.path.join(script_directory, "pokemon_stats.json")
team_centroids_path = os.path.join(script_directory, "team_centroids_scores.json")

# Given time, consider modifying this code to have 

# This creates the file if it doesn't already exist,
# or erases its contents if it does exist
open(team_centroids_path, 'w').close()

team_centroids_list = []
with open(team_scores_path, 'r') as file_scores:
    data_teams = json.load(file_scores)
    with open(pokemon_stats_path, 'r') as file_stats:
        data_stats = json.load(file_stats)
        # print(data_stats)

        for team in data_teams:
            score = team[1]
            print(f"Team: {team[0]}, Score: {score}")

            # The team is converted into a string when read off from json, so we need to convert it back into a list
            # to get the stats for each pokemon in the team
            team_comp = eval(team[0])

            print(team_comp)

            stats_lists = [data_stats[key.lower()] for key in team_comp]
            transposed = zip(*stats_lists)
            means = [mean(group) for group in transposed]

            output = [team_comp, means, score]
            team_centroids_list.append(output)

        file_stats.close()
    file_scores.close()

with open(team_centroids_path, 'w') as file_centroids:
    json.dump(team_centroids_list, file_centroids)
    file_centroids.close()