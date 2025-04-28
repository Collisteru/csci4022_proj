import math

wins = 0

losses = 100

n = wins + losses

p = wins / n if n > 0 else 0

z = 1.64 # 95% Confidence interval

# Special cases required for p = 1and p = 0



team_score = (wins + 1) / (wins + losses + 2)

print(f"Wins: {wins}, Losses: {losses}, Team Score: {team_score}")