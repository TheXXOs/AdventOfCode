f = open("in.txt", "r")
score = 0
for line in f.read().split("\n"):
    if line[-1] == "X":
        score += 1
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 0
        elif line[0] == "C":
            score += 6
            
    elif line[-1] == "Y":
        score += 2
        if line[0] == "A":
            score += 6
        elif line[0] == "B":
            score += 3
        elif line[0] == "C":
            score += 0
    elif line[-1] == "Z":
        score += 3
        if line[0] == "A":
            score += 0
        elif line[0] == "B":
            score += 6
        elif line[0] == "C":
            score += 3
print(score)
