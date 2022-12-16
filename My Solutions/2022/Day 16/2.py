import re

f = open("in.txt", "r")
file = f.read().splitlines()

valves = {}
for line in file:
    l = line.split(" ")
    valves[l[1]] = (int(l[4][5:-1]),set([x.replace(",","") for x in l[9:]]))
print(valves)
paths = [("AA",0,set(),"AA")] # each val is (location, flow, (open), elephant)

def calcflow(path):
    out = 0
    for opn in path[2]:
        out += valves[opn][0]
    return path[1] + out

reducecap = 1000 # increasing this gets a more accurate answer but takes longer

for i in range(26): # bruteforce my belo(v/ath)ed
    newpaths = []
    for path in paths:
        # YOU AND ELEPHANT OPEN
        if path[0] not in path[2] and valves[path[0]][0] != 0 and path[3] not in path[2] and valves[path[3]][0] != 0: # if valve not open
            q = set(path[2])
            q.add(path[0])
            q.add(path[3])
            newpaths.append((path[0],calcflow(path),q,path[3])) # open valve
        # JUST YOU OPEN
        if path[3] not in path[2] and valves[path[3]][0] != 0:
            for loc in valves[path[0]][1]:
                q = set(path[2])
                q.add(path[3])
                newpaths.append((loc,calcflow(path),q,path[3]))
        # JUST ELEPHANT OPEN
        if path[0] not in path[2] and valves[path[0]][0] != 0:
            for loc in valves[path[3]][1]:
                q = set(path[2])
                q.add(path[0])
                newpaths.append((path[0],calcflow(path),q,loc))
        # BOTH MOVE
        for loc in valves[path[0]][1]: # for each possible location
            for loca in valves[path[3]][1]:
                newpaths.append((loc,calcflow(path),path[2],loca)) # move there
    paths = []
    [paths.append(x) for x in newpaths if x not in paths]
    paths = sorted(paths,key=lambda t: t[1])
    if len(paths) > reducecap:
        paths = paths[-reducecap:] # naive data reducing, aka gambling on whether i get the right answer
    print(i,len(paths))
    print(paths[-1])
print("Final pressure of",paths[-1][1],"but there may be a small chance of it being incorrect")
