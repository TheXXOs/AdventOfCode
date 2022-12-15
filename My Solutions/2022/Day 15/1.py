import re

f = open("in.txt", "r")
file = f.read().splitlines()

def manhattan(sx,sy,bx,by):
    return abs(sx-bx)+abs(sy-by)

sensors = set()
beacons = set()
for line in file:
    sx,sy,bx,by = [int(x) for x in re.findall('-?\d+',line)]
    sensors.add((sx,sy,manhattan(sx,sy,bx,by)))
    beacons.add((bx,by))

total = 0
for x in range(-1020000,5000000):
    if x % 100000 == 0:
        print(x)
    for sx,sy,m in sensors:
        if manhattan(sx,sy,x,2000000) <= m:
            if (x,2000000) not in beacons:
                total += 1
            break
print("There are",total,"locations where beacons cannot be")
