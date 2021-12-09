# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
inp = [list(i) for i in inp]
basins = []
checked = []
def findBasin(i,j):
    global inp
    global checked
    total = 0
    checkNext = []
    for x in [[i,j+1],[i+1,j],[i-1,j],[i,j-1]]:
        try:
            if (int(inp[x[0]][x[1]]) != 9) and (x not in checked) and (int(inp[i][j]) < int(inp[x[0]][x[1]])) and int(x[0]) >= 0 and int(x[1]) >= 0:
                total += 1
                checkNext.append(x)
                checked.append(x)
        except:
            pass
    for x in checkNext:
        total += findBasin(x[0],x[1])
    return total

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
            checked.append([i,j])
            basins.append(1 + findBasin(i,j))
output = 1
for i in sorted(basins, reverse=True)[:3]:
    output *= i
print(output)
