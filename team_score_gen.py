import json

def get_team_wins_losses():
    path  = "./battle_summaries.json" 

    with open(path, 'r') as f:
        data = json.load(f)
        team_win_rate = {}
        for i, triple in enumerate(data):
            team1 = str(triple[0])
            team2 = str(triple[1])
            team1_win = triple[2]

            if team1 not in team_win_rate:
                if team1_win:
                    team_win_rate[team1] = {"wins": 1, "losses": 0}
                else:
                    team_win_rate[team1] = {"wins": 0, "losses": 1}
            else:
                if team1_win:
                    team_win_rate[team1]["wins"] += 1
                else:
                    team_win_rate[team1]["losses"] += 1

            if team2 not in team_win_rate:
                if team1_win:
                    team_win_rate[team2] = {"wins": 0, "losses": 1}
                else:
                    team_win_rate[team2] = {"wins": 1, "losses": 0}
            else:
                if team1_win:
                    team_win_rate[team2]["losses"] += 1
                else:
                    team_win_rate[team2]["wins"] += 1

        output_path = "./team_wins_losses.json"
        with open(output_path, 'w') as output:
            json.dump(team_win_rate, output)
            output.close()


def get_scores_from_wins_losses():
    path  = "./team_wins_losses.json" 

    # Apply the Wilson Score interval correction (Binomial proportion confidence interval) to deal with the varying sample sizes of various teams

    with open(path, 'r') as f:
        data = json.load(f)
        team_win_rate = {}
        for team, record in data.items():
            wins = record["wins"]
            losses = record["losses"]
            total = wins + losses
            win_rate = (wins + 1) / (wins + losses + 2) if total > 0 else 0
            team_win_rate[team] = win_rate

        output_path = "./team_scores.json"
        with open(output_path, 'w') as output:
            json.dump(team_win_rate, output)
            output.close()

get_scores_from_wins_losses()