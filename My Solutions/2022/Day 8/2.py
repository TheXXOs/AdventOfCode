f = open("in.txt", "r")
file = f.read().splitlines()
vcount = 0
best = 0
for y in range(len(file)):
    for x in range(len(file[y])):
        vL = 0
        vU = 0
        vR = 0
        vD = 0
        for i in range(x-1,-1,-1): # search left
            vL += 1
            if int(file[y][i]) >= int(file[y][x]):
                break 
        for i in range(y-1,-1,-1): # search up
            vU += 1
            if int(file[i][x]) >= int(file[y][x]):
                break
        for i in range(x+1,len(file[y])): # search right
            vR += 1
            if int(file[y][i]) >= int(file[y][x]):
                break
        for i in range(y+1,len(file)): # search down
            vD += 1
            if int(file[i][x]) >= int(file[y][x]):
                break
        if vL*vU*vR*vD > best:
            best = vL*vU*vR*vD
print(best)
