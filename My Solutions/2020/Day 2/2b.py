f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
validP = 0
for i in cList:
    ia = i.split()
    ias = ia[0].split("-")
    posA = int(ias[0])
    posB = int(ias[1])
    #ia[2] is the string, ia[1] is the letter
    if (ia[2][posA-1] == ia[1][0]) != (ia[2][posB-1] == ia[1][0]):
        validP += 1
print(validP)
