# Mapping the Metagame: A Data-driven Analysis of the Pokémon Showdown Competitive Scene
Analysis of the Pokémon Showdown Competitive Scene

## Format:

* Generation 9 VGC, since it's the current official format

## Coding Logistics:

- Do ./source/Activate to activate the virtual environment (Windows 11 + VSCode + WSL, may be different on your machine)
- If you wish to reproduce these results without already having the zip and json files created, the correct order to run the files is:
[`battle_id_scraper.py`](battle_id_scraper.py), [`battle_data_scraper.py`](battle_data_scraper.py), [`battle_data_congregator.py`](battle_data_congregator.py), [`stat_scraper.py`](stat_scraper.py), [`centroid_finder.py`](centroid_finder.py)
- Also note that collecting these data yourself may introduce problems in the stat_scraper file as many Pokémon names had to be manually corrected

## Sources:

* API: 
https://github.com/smogon/pokemon-showdown-client/blob/master/WEB-API.md


* API Search URL:
https://replay.pokemonshowdown.com/search.json?format=[Gen%209]%20VGC%202025%20Reg%20G%20(Bo3

* Single Battle Example:
https://replay.pokemonshowdown.com/gen9vgc2025reggbo3-2332373833.json

Pagination seems to be the best way to scrape, although they say it's no longer supported:

https://replay.pokemonshowdown.com/search.json?format=[Gen%209]%20VGC%202025%20Reg%20G%20(Bo3&page=3

## Data Collection:

* 100 pages of 50 battles each in our chosen format are available to us, meaning we have a battle dataset totalling 5000. 

- Code a scraper to get all the IDs of the battles in the format

- Code a scaper to get all the data from each of these battles. 

## Data Collection Questions:

* What is the minimum timestamp of a battle?

