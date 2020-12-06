#day 6
#lets go, part 1 was easy

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
cList.append("")

totalYes = 0
groupYes = []
groupLen = 0
for line in cList:
    counted = []
    if line != "":
        for char in line:
            groupYes.append(char)
        groupLen += 1
    else:
        for i in groupYes:
            if (not i in counted) and groupYes.count(i) == groupLen:
                counted.append(i)
        totalYes += len(counted)
        groupYes = []
        groupLen = 0
print(totalYes)
