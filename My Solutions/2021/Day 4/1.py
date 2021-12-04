import re
# begin opening code
with open("in.txt") as f:
    inp = f.read().split('\n\n')
# end opening code

# put daily code below here, copy this file for part 2
squares = inp[0].split(",")
inp = [j.split("\n") for j in inp[1:]]
for i in range(len(inp)):
    inp[i] = [re.split(r'\s+',j.strip()) for j in inp[i]]

def checkwin(inp):
    for i in inp:
        for j in i:
            if j == ["X","X","X","X","X"]:
                return True
        for j in range(5):
            if i[0][j] == "X" and i[1][j] == "X" and i[2][j] == "X" and i[3][j] == "X" and i[4][j] == "X":
                return True
last = ""
board = 0
for i in squares:
    for j in range(len(inp)):
        for k in range(len(inp[j])):
            for l in range(len(inp[j][k])):
                if inp[j][k][l] == i:
                    last = i
                    board = inp[j]
                    inp[j][k][l] = "X"
                if checkwin(inp):
                    total = 0
                    for j in board:
                        for k in j:
                            if k != "X":
                                total += int(k)
                    print(total)
                    print(int(last)*total)
                    print("=============")
                
#print(squares)
print(inp)

# put daily code above here
