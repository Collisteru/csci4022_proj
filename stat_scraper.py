import json
import requests
import os



def get_stats(response_data):
    data = response_data["stats"]
    stats = []
    for i in range(6):
        stats.append(data[i]["base_stat"])
    return stats

# This function corrects the many naming differences between
# Pokemon Showdown and the PokeAPI service
def fix_name(pokemon_name):
    pokemon_name_corrected = pokemon_name.replace(' ', '-')
    # This accounts for the discrepancy between Urshifu
    # being displayed in battle without information on its form,
    # versus the API needing to know its form
    # This distinction does not matter here because
    # there is no difference in stats between the two forms
    if pokemon_name == "urshifu-*":
        pokemon_name_corrected = "urshifu-rapid-strike"
    # These forms are used significantly more often so they will be the default
    elif pokemon_name == "giratina":
        pokemon_name_corrected = "giratina-origin"
    elif pokemon_name == "landorus":
        pokemon_name_corrected = "landorus-incarnate"
    elif pokemon_name == "tornadus":
        pokemon_name_corrected = "tornadus-incarnate"
    elif pokemon_name == "thundurus":
        pokemon_name_corrected = "thundurus-incarnate"
    elif pokemon_name == "enamorus":
        pokemon_name_corrected = "enamorus-therian"
    elif pokemon_name == "basculegion":
        pokemon_name_corrected = "basculegion-male"
    elif pokemon_name == "zacian-*":
        pokemon_name_corrected = "zacian-crowned"
    elif pokemon_name == "zamazenta-*":
        pokemon_name_corrected = "zamazenta-crowned"
    # These have different stats depending on their gender
    elif pokemon_name == "indeedee-f" or pokemon_name == "indeedee":
        pokemon_name_corrected = "indeedee-female"
    elif pokemon_name == "indeedee-m":
        pokemon_name_corrected = "indeedee-male"
    elif pokemon_name == "meowstic-f" or pokemon_name == "meowstic":
        pokemon_name_corrected = "meowstic-female"
    elif pokemon_name == "meowstic-m":
        pokemon_name_corrected = "meowstic-male"
    elif pokemon_name == "basculegion-f":
        pokemon_name_corrected = "basculegion-female"
    elif pokemon_name == "oinkologne-f" or pokemon_name == "oinkologne":
        pokemon_name_corrected = "oinkologne-female"
    elif pokemon_name == "oinkologne-m":
        pokemon_name_corrected = "oinkologne-male"
    # General name corrections
    elif pokemon_name == "mimikyu":
        pokemon_name_corrected = "mimikyu-disguised"
    elif pokemon_name == "lycanroc":
        pokemon_name_corrected = "lycanroc-midday"
    elif pokemon_name == "necrozma-dawn-wings":
        pokemon_name_corrected = "necrozma-dawn"
    elif pokemon_name == "necrozma-dusk-mane":
        pokemon_name_corrected = "necrozma-dusk"
    elif pokemon_name == "toxtricity":
        pokemon_name_corrected = "toxtricity-amped"
    elif pokemon_name == "morpeko":
        pokemon_name_corrected = "morpeko-full-belly"
    elif pokemon_name == "tatsugiri":
        pokemon_name_corrected = "tatsugiri-droopy"
    elif pokemon_name == "palafin":
        pokemon_name_corrected = "palafin-hero"
    elif pokemon_name == "sinistcha-masterpiece":
        pokemon_name_corrected = "sinistcha"
    # These have multiple forms, but they all share the same stats
    elif "pikachu" in pokemon_name:
        pokemon_name_corrected = "pikachu"
    elif "gastrodon" in pokemon_name:
        pokemon_name_corrected = "gastrodon"
    elif "sawsbuck" in pokemon_name:
        pokemon_name_corrected = "sawsbuck"
    elif "greninja" in pokemon_name:
        pokemon_name_corrected = "greninja"
    elif "vivillon" in pokemon_name:
        pokemon_name_corrected = "vivillon"
    elif "florges" in pokemon_name:
        pokemon_name_corrected = "florges"
    elif "minior" in pokemon_name:
        pokemon_name_corrected = "minior-red-meteor"
    elif "oricorio" in pokemon_name:
        pokemon_name_corrected = "oricorio-baile"
    elif "alcremie" in pokemon_name:
        pokemon_name_corrected = "alcremie"
    elif "maushold" in pokemon_name:
        pokemon_name_corrected = "maushold-family-of-four"
    elif "tauros-paldea" in pokemon_name:
        pokemon_name_corrected += "-breed"
    elif "dudunsparce" in pokemon_name:
        pokemon_name_corrected = "dudunsparce-two-segment"
    elif "ogerpon" in pokemon_name:
        pokemon_name_corrected = "ogerpon"
    
    return pokemon_name_corrected



script_directory = os.path.dirname(os.path.abspath(__file__))
battle_summaries_path = os.path.join(script_directory, "battle_summaries.json")
pokemon_stats_path = os.path.join(script_directory, "pokemon_stats.json")
# This creates the file if it doesn't already exist,
# or erases its contents if it does exist
open(pokemon_stats_path, 'w').close()

pokemon_stats_dict = {}
with open(battle_summaries_path, 'r') as file_battles:
    data_battles = json.load(file_battles)
    for battle in data_battles:
        teams = battle[0] + battle[1]
        for pokemon_name_upper in teams:
            pokemon_name = pokemon_name_upper.lower()
            if not pokemon_name in pokemon_stats_dict:
                pokemon_name_corrected = fix_name(pokemon_name)
                # API call
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_corrected}")
                if response.status_code == 200:
                    output = get_stats(response.json())
                    pokemon_stats_dict[pokemon_name] = output
                    # This process takes a bit so seeing this progress is nice
                    print(pokemon_name_corrected)
                else:
                    print(f"Could not retrieve data of {pokemon_name_corrected}")
                    print(f"Error code: {response.status_code}")

with open(pokemon_stats_path, 'w') as file_stats:
    json.dump(pokemon_stats_dict, file_stats)
    file_stats.close()
file_battles.close()
