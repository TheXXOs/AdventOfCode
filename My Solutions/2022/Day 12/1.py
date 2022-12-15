import time
f = open("in.txt", "r")
file = f.read().splitlines()
# part a - extract start + end points
for y in range(len(file)):
    for x in range(len(file[y])):
        if file[y][x] == "S":
            start = (x, y)
            file[y] = file[y].replace("S","a")
        if file[y][x] == "E":
            end = (x, y)
            file[y] = file[y].replace("E","z")
def search(x,y,dx,dy):
    try:
        return ord(file[y+dy][x+dx])-ord(file[y][x]) <= 1
    except IndexError:
        return False
visited = set()
searchfrom = {start}
newsf = {}
moves = 0
while end not in searchfrom:
    moves += 1
    newsf = set(searchfrom)
    for (x,y) in searchfrom:
        newsf.remove((x,y))
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if search(x,y,dx,dy) and (x+dx,y+dy) not in visited and (x+dx,y+dy) not in searchfrom:
                visited.add((x,y))
                newsf.add((x+dx,y+dy))
    searchfrom = newsf
    #visualisation
    ''' # remove this \''' to use the visualisation
    out = ""
    for y in range(len(file)):
        for x in range(len(file[y])):
            if (x,y) == start:
                out += "S"
            elif (x,y) in searchfrom:
                out += "▒"
            elif (x,y) in visited:
                out += "█"
            elif (x,y) == end:
                out += "⚑"
            else:
                out += file[y][x]
        out += "\n"
    print(out)
    time.sleep(0.01)
    #'''
print(moves)
