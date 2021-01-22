#day 11
#i'm going on holiday tomorrow :(
import copy

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
cLList = [list(i) for i in cList]

def stepGrid(grid):
    def checkAdjacent(xPos,yPos):
        aCount = 0
        if xPos > 0:
            if yPos > 0:
                if oldGrid[yPos-1][xPos-1] == "#":
                    aCount += 1
            if yPos < len(grid)-1:
                if oldGrid[yPos+1][xPos-1] == "#":
                    aCount += 1
            if oldGrid[yPos][xPos-1] == "#":
                aCount += 1
        if xPos < len(grid[0])-1:
            if yPos > 0:
                if oldGrid[yPos-1][xPos+1] == "#":
                    aCount += 1
            if yPos < len(grid)-1:
                if oldGrid[yPos+1][xPos+1] == "#":
                    aCount += 1
            if oldGrid[yPos][xPos+1] == "#":
                aCount += 1
        if yPos < len(grid)-1:
            if oldGrid[yPos+1][xPos] == "#":
                aCount += 1
        if yPos > 0:
            if oldGrid[yPos-1][xPos] == "#":
                aCount += 1
        return aCount
    
    oldGrid = copy.deepcopy(grid)
    for (n,y) in enumerate(grid):
        for (m,x) in enumerate(y):
            if checkAdjacent(m,n) == 0 and x == "L":
                grid[n][m] = "#"
            elif checkAdjacent(m,n) >= 4 and x == "#":
                grid[n][m] = "L"
    return grid

oldC = []
while oldC != cLList:
    oldC = copy.deepcopy(cLList)
    cLList = stepGrid(cLList)

fillCount = 0
for y in cLList:
    for x in y:
        if x == "#":
            fillCount += 1
print(fillCount)
