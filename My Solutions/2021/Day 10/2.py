# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
# inp = [int(i) for i in inp]
scores = []
points = {
    "*": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
for i in inp:
    lscore = 0
    corrupt = False
    look = []
    j = i.replace(")","*") # so i can use ord() consistently
    for char in list(j):
        if char in {"(","[","{","<"}:
            look.append(char)
        else:
            if not ord(look[-1]) == ord(char)-2:
                corrupt = True
                break
            else:
                look.pop()
    if not corrupt:
        look.reverse()
        for i in look:
            lscore *= 5
            lscore += points[chr(ord(i)+2)]
        scores.append(lscore)
sscores = sorted(scores)
print(sscores[len(sscores)//2])
