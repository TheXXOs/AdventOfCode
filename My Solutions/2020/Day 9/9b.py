#day 9
#i did *not* read the question correctly

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
targetedNums = cList[:25]
for i in cList[25:]:
    comboFound = False
    for j in targetedNums:
        for k in targetedNums:
            if j!=k and int(j)+int(k)==int(i):
                comboFound = True
    if not comboFound:
        invalidNum = i
        break
    targetedNums = targetedNums[1:]
    targetedNums.append(i)
bFound = False
cLInt = [int(i) for i in cList]
for (i,first) in enumerate(cList): #i is order, first is value
    for j in range(i+1,len(cList)):
        sumi = sum(cLInt[i:j])
        if sumi == int(invalidNum):
            bFound = True
            si = i
            sj = j
            break
    if bFound:
        print(max(cLInt[si:sj])+min(cLInt[si:sj]))
        break
