#day 11
#why did part one take so loooooooong
import copy

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
cLList = [list(i) for i in cList]


def stepGrid(grid):
    def adjSeat(xPos,yPos,xDir,yDir):
        try:
            if yPos+yDir >= 0 and xPos+xDir >= 0:
                if oldGrid[yPos+yDir][xPos+xDir] == ".":
                    return adjSeat(xPos+xDir,yPos+yDir,xDir,yDir)
                else:
                    return oldGrid[yPos+yDir][xPos+xDir]
            else:
                return "L"
        except:
            return "L"
    def checkAdjacent(xPos,yPos):
        aCount = [adjSeat(xPos,yPos,dx,dy) for (dx,dy) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]].count('#')
        return aCount
    
    oldGrid = copy.deepcopy(grid)
    for (n,y) in enumerate(grid):
        for (m,x) in enumerate(y):
            if checkAdjacent(m,n) == 0 and x == "L":
                grid[n][m] = "#"
            elif checkAdjacent(m,n) >= 5 and x == "#":
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
