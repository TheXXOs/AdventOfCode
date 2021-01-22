#day 12
#hehe gold coast go brr

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

position = [1,10] # n/s, e/w; waypoint position relative to ship
shipPos = [0,0]

for i in cList:
    j = i[0]
    k = int(i[1:])
    if j in ("L","R"):
        if j == "L":
            k = 360 - k
        ki = int(k/90)
        for i in range(ki):
            position = [-position[1],position[0]]
    elif j == "N":
        position[0] += k
    elif j == "S":
        position[0] -= k
    elif j == "E":
        position[1] += k
    elif j == "W":
        position[1] -= k
    elif j == "F":
        for x in range(k):
            shipPos[0] += position[0]
            shipPos[1] += position[1]
print(abs(shipPos[0])+abs(shipPos[1]))
