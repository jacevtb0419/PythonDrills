games = [
    {"Name": "UD", "Score": 27, "Away?": False},
    {"Name": "Clemson", "Score": 14, "Away?": True},
    {"Name": "Pitt", "Score": 32, "Away?": True},
]
score = 0
for game in games: 
    score = game["Score"] + score
    
print(score)

