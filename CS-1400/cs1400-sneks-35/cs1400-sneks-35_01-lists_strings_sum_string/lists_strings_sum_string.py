scores = "44,34,27,43,22,25"
total_score = 0
for a_score in scores.split(","):
    total_score = int(a_score) + total_score
print(total_score)
