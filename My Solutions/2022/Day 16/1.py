import re

f = open("in.txt", "r")
file = f.read().splitlines()

valves = {}
for line in file:
    l = line.split(" ")
    valves[l[1]] = (int(l[4][5:-1]),set([x.replace(",","") for x in l[9:]]))
print(valves)
paths = [("AA",0,set())] # each val is (location, flow, (open))

def calcflow(path):
    out = 0
    for opn in path[2]:
        out += valves[opn][0]
    return path[1] + out

for i in range(30): # bruteforce my belo(v/ath)ed
    newpaths = []
    for path in paths:
        if path[0] not in path[2] and valves[path[0]][0] != 0: # if valve not open
            q = set(path[2])
            q.add(path[0])
            newpaths.append((path[0],calcflow(path),q)) # open valve
        for loc in valves[path[0]][1]: # for each possible location
            newpaths.append((loc,calcflow(path),path[2])) # move there
    paths = []
    [paths.append(x) for x in newpaths if x not in paths]
    paths = sorted(paths,key=lambda t: t[1])
    if i%10 == 0 or i >= 14: # naive data reducing, aka gambling on whether i get the right answer
        paths = paths[len(paths)//2:]
    print(i,len(paths))
    print(paths[-1])
print("Final pressure of",paths[-1][1],"but there may be a small chance of it being incorrect")
