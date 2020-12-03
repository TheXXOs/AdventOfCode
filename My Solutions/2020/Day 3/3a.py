#day 3
#aaa im late help
f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
i = 0
treeCount = 0
for line in cList:
    if line[i] == "#":
        treeCount += 1
    i += 3
    i %= len(line)
print(treeCount)
