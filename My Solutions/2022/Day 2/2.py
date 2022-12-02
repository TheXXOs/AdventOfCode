f = open("in.txt", "r")
score = 0
for line in f.read().split("\n"):
    if line[-1] == "X":
        # score += 0
        if line[0] == "A": # A X = lose on rock = scissors
            score += 3
        elif line[0] == "B": # B X = lose on paper = rock
            score += 1
        elif line[0] == "C":
            score += 2     
    elif line[-1] == "Y":
        score += 3
        if line[0] == "A":
            
            score += 1
        elif line[0] == "B":
            score += 2
        elif line[0] == "C":
            score += 3

    elif line[-1] == "Z":
        score += 6
        if line[0] == "A":
            score += 2
        elif line[0] == "B":
            score += 3
        elif line[0] == "C":
            score += 1
print(score)
