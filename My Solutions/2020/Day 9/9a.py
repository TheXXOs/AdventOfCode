#day 9
#a smidge late, not too bad tho

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
        print(i)
        break
    targetedNums = targetedNums[1:]
    targetedNums.append(i)
