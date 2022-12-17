import re
import sys

f = open("in.txt", "r")
file = f.read().splitlines()

def manhattan(sx,sy,bx,by):
    return abs(sx-bx)+abs(sy-by)

def revManhattan(sx,sy,m):
    out = []
    for i in range(m+1):
        out.append((i,m-i))
    out = out + [(-x,y) for (x,y) in out] + [(x,-y) for (x,y) in out] + [(-x,-y) for (x,y) in out]
    return set([(sx+x,sy+y) for (x,y) in out])

sensors = set()
beacons = set()
for line in file:
    sx,sy,bx,by = [int(x) for x in re.findall('-?\d+',line)]
    sensors.add((sx,sy,manhattan(sx,sy,bx,by)))
    beacons.add((bx,by))

# old, slow code
'''for x in range(100000,3900000):
    for y in range(100000,3900000):
        if y % 100000 == 0:
            print(x,y)
        sensed = False
        for sx,sy,m in sensors:
            if manhattan(sx,sy,x,y) <= m:
                sensed = True
                break
        if not sensed:
            print("Beacon is at",x,y,"with frequency",x*4000000+y)
            sys.exit()'''

print(sensors)
'''toSearch = set()
for (sx,sy,m) in sensors:
    toSearch = toSearch.union(revManhattan(sx,sy,m+1))
vis = set()
for (sx,sy,m) in sensors:
    vis = vis.union(revManhattan(sx,sy,m))
sensorsy = [(x,y) for (x,y,m) in sensors]'''
for (sx,sy,m) in sensors:
    for beacon in beacons:
        if manhattan(sx,sy,beacon[0],beacon[1]) == m:
            bx, by = beacon[0], beacon[1]
    toSearch = revManhattan(sx,sy,m+1)
    vis = revManhattan(sx,sy,m)
    for y in range(21):
        for x in range(21):
            if (x,y) == (bx,by):
                print("B",end="")
            elif (x,y) == (sx,sy):
                print(next(obj for obj in list(sensors) if obj[0] == x and obj[1] == y)[2],end="")
            elif (x,y) in vis and (x,y) in toSearch:
                print("█", end="")
            elif (x,y) in vis:
                print("▓",end="")
            elif (x,y) in toSearch:
                print("░",end="")
            else:
                print(" ",end="")
        print()
    print("====================")

# new, faster (hopefully) code!
#    instead of looking through all of the possible points,
#    i'm instead just looking at the points that are a
#    manhattan distance + 1 away from the sensors
#    it's not working though :(
'''for (sx,sy,m) in sensors:
    print("Searching from x",sx,"y",sy,"r",m)
    for (searchx, searchy) in revManhattan(sx,sy,m+1):
        sensed = False
        if searchx <= 20 and searchx >= 0 and searchy <= 20 and searchy >= 0:
            for (ssx,ssy,sm) in sensors:
                if manhattan(ssx,ssy,searchx,searchy) <= sm:
                    sensed = True
                    break
        if not sensed and searchx <= 20 and searchx >= 0 and searchy <= 20 and searchy >= 0:
            print(searchx, searchy)
            print("Frequency:",searchx*400000+searchy)
            sys.exit()'''
