import sys
sys.setrecursionlimit(1000)

f = open("in.txt", "r")
file = f.read().splitlines()
sides = 0
maxx = 2
maxy = 2
maxz = 2
bubbles = set()
# get max x, y, z values (min is 0 as there are no negatives)
for cube in file:
    cs = cube.split(",")
    x = int(cs[0])
    y = int(cs[1])
    z = int(cs[2])
    if x > maxx: maxx = x
    if y > maxy: maxy = y
    if z > maxz: maxz = z

#print(maxx,maxy,maxz,maxx*maxy*maxz)

checked = set()
toCheck = {(0,0,0)}
while len(toCheck) > 0:
    newCh = set()
    for x,y,z in toCheck:
        #print("checking",x,y,z)
        checked.add((x,y,z))
        for diff in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            xx = x+diff[0]
            yy = y+diff[1]
            zz = z+diff[2]
            if xx <= maxx+1 and yy <= maxy+1 and zz <= maxz+1 and xx >= -1 and yy >= -1 and zz >= -1:
                if str(xx)+","+str(yy)+","+str(zz) in file:
                    sides += 1
                elif (xx,yy,zz) not in checked:
                    newCh.add((xx,yy,zz))
    toCheck = set(newCh)
print(sides)

"""def steamSim(x,y,z):
    global sides
    global checked
    global breakify
    if not breakify:
        checked.add((x,y,z))
        for diff in {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}:
            xx = x+diff[0]
            yy = y+diff[1]
            zz = z+diff[2]
            if xx <= maxx+1 and yy <= maxy+1 and zz <= maxz+1 and xx >= -1 and yy >= -1 and zz >= -1:
                if str(xx)+","+str(yy)+","+str(zz) in file:
                    #print("side of",xx,yy,zz,"found from",x,y,z)
                    sides += 1
                elif (xx,yy,zz) not in checked:
                    try:
                        steamSim(xx,yy,zz)
                    except RecursionError:
                        print("break",max(checked,key=lambda x:x[2]))
                        breakify = True
                        break
            else: # out of map, can't search
                pass"""

"""
def isItBubble(xx,yy,zz):
    knowns.add((xx,yy,zz))
    for difff in {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}: # search in all directions
        if (xx,yy,zz) in bubbles:
            for i in knowns:
                bubbles.add(i)
            return True
        if (xx+difff[0],yy+difff[1],zz+difff[2]) not in knowns: # if not already searched
            if not (xx+difff[0] > maxx or yy+difff[1] > maxy or zz+difff[2] > maxz or xx+difff[0] < 0 or yy+difff[1] < 0 or zz+difff[2] < 0): # if not touching edge of map
                if str(xx+difff[0])+","+str(yy+difff[1])+","+str(zz+difff[2]) not in file: # if it is air
                    return isItBubble(xx+difff[0],yy+difff[1],zz+difff[2])
                else: # it's solid
                    pass
            else: # touches edge of map ("air bubble" isn't an air bubble)
                return False
        else: # already searched
            pass
    # all of the directions were either already searched or solid - it's a bubble?
    for i in knowns:
        bubbles.add(i)
    return True # unsure if this is the right thing to do???

for cube in file:
    cs = cube.split(",")
    x = int(cs[0])
    y = int(cs[1])
    z = int(cs[2])
    for diff in {(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}:
        if str(x+diff[0])+","+str(y+diff[1])+","+str(z+diff[2]) not in file:
            knowns = set()
            if not isItBubble(x+diff[0],y+diff[1],z+diff[2]):
                sides += 1"""
