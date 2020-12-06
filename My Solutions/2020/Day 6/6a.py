#day 6
#i was late bc MINECRAFT

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
cList.append("")

totalYes = 0
groupYes = []
for line in cList:
    if line != "":
        for char in line:
            if not char in groupYes:
                groupYes.append(char)
    else:
        totalYes += len(groupYes)
        groupYes = []
print(totalYes)
