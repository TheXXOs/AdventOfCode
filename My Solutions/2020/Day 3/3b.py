#day 3
#aaa im late help
f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
i = 0
treeCountA = 0
treeCountB = 0
treeCountC = 0
treeCountD = 0
treeCountE = 0
for line in cList:
    if line[i] == "#":
        treeCountA += 1
    i += 1
    i %= len(line)
i = 0
for line in cList:
    if line[i] == "#":
        treeCountB += 1
    i += 3
    i %= len(line)
i = 0
for line in cList:
    if line[i] == "#":
        treeCountC += 1
    i += 5
    i %= len(line)
i = 0
for line in cList:
    if line[i] == "#":
        treeCountD += 1
    i += 7
    i %= len(line)
i = 0
j = 0
for line in cList:
    if j%2 == 0:
        if line[i%len(line)] == "#":
            treeCountE += 1
        i += 1
    j += 1
treeCount = treeCountA*treeCountB*treeCountC*treeCountD*treeCountE
print(treeCount)
