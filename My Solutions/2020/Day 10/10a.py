#day 10
#hopefully a day with no issues!
#p.s. i'm not going to be able to do 12-17 on time :(

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
cLInt = [int(i) for i in cList]
f.close()

cLInt.sort()
cLInt.append(max(cLInt)+3)
mostRecent = 0
oneJolt = 0
threeJolt = 0
for i in cLInt:
    if i-mostRecent==1:
        oneJolt+=1
    elif i-mostRecent==3:
        threeJolt+=1
    mostRecent = i
print(oneJolt*threeJolt)
