#day 12
#hehe gold coast go brr

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

facing = 0 # east
position = [0,0] # n/s 0, e/w 0

for i in cList:
    j = i[0]
    k = int(i[1:])
    if j in ("L","R"):
        if j == "L":
            k = 360 - k
        facing += k
        facing %= 360
    elif j == "N":
        position[0] += k
    elif j == "S":
        position[0] -= k
    elif j == "E":
        position[1] += k
    elif j == "W":
        position[1] -= k
    elif j == "F":
        if facing == 0: #east
            position[1] += k
        elif facing == 90: #south
            position[0] -= k
        elif facing == 180: #west
            position[1] -= k
        elif facing == 270: #north
            position[0] += k
print(abs(position[0])+abs(position[1]))
