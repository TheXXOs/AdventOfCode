# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
# inp = [int(i) for i in inp]
score = 0
points = {
    "*": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
new = []
for i in inp:
    look = []
    j = i.replace(")","*") # so i can use ord() consistently
    for char in list(j):
        if char in {"(","[","{","<"}:
            look.append(char)
        else:
            if not ord(look[-1]) == ord(char)-2:
                score += points[char]
                break
            else:
                look.pop()
print(score)
