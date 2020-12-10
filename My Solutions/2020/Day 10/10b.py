#day 10
#this took a while, thx flumble again again again

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
cLInt = [int(i) for i in cList]
f.close()

cLInt.sort()
cLInt.append(max(cLInt)+3)
cLInt.reverse()
cLInt.append(0)
ways = 0
cWays = {}
for (n,i) in enumerate(cLInt):
    if n == 0 or n == 1: #"final" and "second-to-last" item
        cWays[i] = 1
    elif n >= 2: #"third-to-last" and "lower" items
        cWays[i] = 0
        if cLInt[n-1]-i<=3:
            cWays[i] = cWays[i]+cWays[cLInt[n-1]]
        if cLInt[n-2]-i<=3:
            cWays[i] = cWays[i]+cWays[cLInt[n-2]]
        if cLInt[n-3]-i<=3 and n > 2:
            cWays[i] = cWays[i]+cWays[cLInt[n-3]]
print(cWays[0])
