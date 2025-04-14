import os
import zipfile
import json
import re



# Ensure that the zip file is found in this file's directory,
# rather than the environment's running directory
script_directory = os.path.dirname(os.path.abspath(__file__))
battle_zip_path = os.path.join(script_directory, "battle_data.zip")

# Read in the zip file as well as the first entry (for testing)
battle_data = zipfile.ZipFile(battle_zip_path, "r")

# Iterate over all battles to summarize the data
battle_summaries = []
for battle_id in battle_data.namelist():
    current_battle = battle_data.read(battle_id)
    current_battle_parsed = json.loads(current_battle)
    log = current_battle_parsed["log"]

    # Due to the battle log being stored as a string,
    # parsing it with manually-defined spacing
    # is necessary for locating useful data
    teamsize_index = log.find("teamsize")
    teamsize_p1 = int(log[teamsize_index+12:teamsize_index+13])
    teamsize_p2 = int(log[teamsize_index+27:teamsize_index+28])

    # Ensure that both teams are full,
    # otherwise this battle is not valid
    if (teamsize_p1 == 6) and (teamsize_p2 == 6):
        # Extract Pokemon names from team listings
        team_comp_index = log.find("|clearpoke")
        team_comp_regex = r"\|poke\|p.\|([^,]+)"
        team_comp = re.findall(team_comp_regex, log[team_comp_index:])
        team_comp_p1 = team_comp[:6]
        team_comp_p1.sort()
        team_comp_p2 = team_comp[6:]
        team_comp_p2.sort()

        # Acquire player names to check against the winner's names at the end
        p1_name_regex = r"\|player\|p1\|([^|]+)"
        p2_name_regex = r"\|player\|p2\|([^|]+)"
        p1_name = re.findall(p1_name_regex, log)[0]
        p2_name = re.findall(p2_name_regex, log)[0]

        # Find the name of the winner of the match
        winner_index = log.find("|win|")
        winner_end_index = log[winner_index + 5:].find("|") + winner_index + 4
        winner_name = log[winner_index + 5:winner_end_index]

        # Store the winner as "Did player 1 win?"
        if winner_name == p1_name:
            winner = True
        else:
            winner = False
        
        # Saved as a tuple for each battle
        # Alternatively, this could exclusively store the winning teams
        # rather than both in a match
        # For now both will be stored in case we find something
        # interesting to do with the worst teams
        battle_summaries.append((team_comp_p1, team_comp_p2, winner))

output_path = os.path.join(script_directory, "battle_summaries.json")
with open(output_path, 'w') as output:
    json.dump(battle_summaries, output)
