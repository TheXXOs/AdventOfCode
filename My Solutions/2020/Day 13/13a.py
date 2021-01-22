#day 13
#what's the term for binging if you're the one doing the work?

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

eTime = int(cList[0])
current = [eTime*100,0]
for i in cList[1].split(","):
    if i != "x":
        ii = int(i)
        j = 0
        while j < eTime:
            j += ii
        if j < current[0]:
            current = [j,ii]
print(current[1]*(current[0]-eTime))
