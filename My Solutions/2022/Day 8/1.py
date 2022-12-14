f = open("in.txt", "r")
file = f.read().splitlines()
vcount = 0
for y in range(len(file)):
    for x in range(len(file[y])):
        sLeft = False
        sUp = False
        sRight = False
        sDown = False
        for i in range(x): # search left
            if int(file[y][i]) >= int(file[y][x]):
                sLeft = True # a taller tree is left
        for i in range(y): # search up
            if int(file[i][x]) >= int(file[y][x]):
                sUp = True # a taller tree is up
        for i in range(x+1,len(file[y])):
            if int(file[y][i]) >= int(file[y][x]):
                sRight = True # a taller tree is right
        for i in range(y+1,len(file)):
            if int(file[i][x]) >= int(file[y][x]):
                sDown = True # a taller tree is down
        if not (sLeft and sRight and sUp and sDown):
            vcount += 1
print(vcount)
