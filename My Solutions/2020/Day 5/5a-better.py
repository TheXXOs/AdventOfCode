#day 5
#i'm dumb, it can be done with replace() and int(base=2)

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

highestID = 0
for i in cList:
    j = i.replace("B","1").replace("F","0").replace("R","1").replace("L","0")
    jbin = int(j, base=2)
    if highestID < jbin:
        highestID = jbin
print(highestID)
