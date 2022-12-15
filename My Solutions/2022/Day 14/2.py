f = open("in.txt", "r")
file = f.read().splitlines()
filled = set()

# input to filled squares
flr = 0
for line in file:
    points = [tuple([int(y) for y in x.split(",")]) for x in line.split(" -> ")] # list of tuples :)
    for i in range(len(points)-1):
        if points[i][0] == points[i+1][0]: # x coords same
            mm = [points[i][1],points[i+1][1]]
            for j in range(min(mm),max(mm)+1):
                filled.add((points[i+1][0],j))
        elif points[i][1] == points[i+1][1]: # y coords same
            mm = [points[i][0],points[i+1][0]]
            for j in range(min(mm),max(mm)+1):
                filled.add((j,points[i][1]))

# find floor
for i in filled:
    if i[1] > flr:
        flr = i[1]
flr += 2

# sand simulation
scoord = (500,0)
sands = 0
while True:
    if scoord[1]+1 == flr: # stop at the floor
        filled.add(scoord)
        scoord = (500,0)
        sands += 1
    else:
        if not (scoord[0],scoord[1]+1) in filled: # try moving down
            scoord = (scoord[0],scoord[1]+1)
        elif not (scoord[0]-1,scoord[1]+1) in filled: # try moving down-left
            scoord = (scoord[0]-1,scoord[1]+1)
        elif not (scoord[0]+1,scoord[1]+1) in filled: # try moving down-right
            scoord = (scoord[0]+1,scoord[1]+1)
        else: # no possible paths, stop moving and restart
            if scoord == (500,0):
                print(sands+1)
                break
            filled.add(scoord)
            scoord = (500,0)
            sands += 1
