f = open("in.txt", "r")
file = f.read().splitlines()
sides = 0
for cube in file:
    cs = cube.split(",")
    x = int(cs[0])
    y = int(cs[1])
    z = int(cs[2])
    for diff in {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}:
        if str(x+diff[0])+","+str(y+diff[1])+","+str(z+diff[2]) not in file:
            sides += 1
print(sides)
