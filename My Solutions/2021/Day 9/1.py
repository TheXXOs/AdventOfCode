# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
inp = [list(i) for i in inp]
risk = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        lowest = True
        try:
            if int(inp[i][j]) >= int(inp[i-1][j]):
                lowest = False
        except:
            pass
        try:
            if int(inp[i][j]) >= int(inp[i+1][j]):
                lowest = False
        except:
            pass
        try:
            if int(inp[i][j]) >= int(inp[i][j-1]):
                lowest = False
        except:
            pass
        try:
            if int(inp[i][j]) >= int(inp[i][j+1]):
                lowest = False
        except:
            pass
        if lowest:
            risk += int(inp[i][j]) + 1
print(risk)
