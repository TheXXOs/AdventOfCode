#day 5
#i'm dumb, it can be done with replace() and int(base=2)

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

seats = []
for i in cList:
    j = i.replace("B","1").replace("F","0").replace("R","1").replace("L","0")
    seatID = int(j, base=2)
    seats.append(seatID)
for i in range(1024):
    if not i in seats and i <= 900 and i >= 100:
        print(i)
