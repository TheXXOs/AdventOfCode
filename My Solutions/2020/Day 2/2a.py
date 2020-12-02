f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
validP = 0
for i in cList:
    ia = i.split()
    ias = ia[0].split("-")
    lowerLim = ias[0]
    upperLim = ias[1]
    if ia[2].count(ia[1][0]) >= int(lowerLim) and ia[2].count(ia[1][0]) <= int(upperLim):
        validP += 1
print(validP)
