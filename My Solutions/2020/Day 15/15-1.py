ip = input("> ")
numDict = {}
count=0
for i in ip.split(","):
    numDict[i] = count
    print(i, count)
    count += 1
lastNum = ip.split(",")[-1]
while count < 2020:
    current = str(count - numDict[lastNum])
    numDict[current] = count
    print(current, count)
    count += 1
    lastNum = current
print(lastNum)
