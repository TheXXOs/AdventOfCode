#day 13
#NOT DONE NOT DONE NOT DONE

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

eTime = int(cList[0])
current = [eTime*100,0]
busList = cList[1].split(",")
t = 100000000000000
busCount = 0
for i in busList:
    if i != "x":
        busCount += 1
while True:
    busesFound = 0
    for (n,i) in enumerate(busList):
        if i != "x":
            if t+n == 0:
                busesFound += 1
            elif int(i)%(t+n) == 0:
                busesFound += 1
    if busesFound == busCount:
        print(t)
        break
    t += 1
print(t)
