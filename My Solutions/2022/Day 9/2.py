f = open("in.txt", "r")

def movetail(headx, heady, tailx, taily):
    if heady != taily and headx != tailx and (abs(heady-taily) >= 2 or abs(headx-tailx) >= 2):
        taily += int((heady-taily)/abs(heady-taily))
        tailx += int((headx-tailx)/abs(headx-tailx))
    elif abs(heady-taily) >= 2:
        taily += int((heady-taily)/abs(heady-taily))
    elif abs(headx-tailx) >= 2:
        tailx += int((headx-tailx)/abs(headx-tailx))
    return tailx, taily

headx = 0
heady = 0
tailxs = [0,0,0,0,0,0,0,0,0]
tailys = [0,0,0,0,0,0,0,0,0]
visited = set()
for line in f.read().splitlines():
    dct = line.split(" ")[0]
    num = int(line.split(" ")[1])
    for i in range(num):
        # move head
        match dct:
            case "R":
                headx += 1
            case "L":
                headx -= 1
            case "U":
                heady += 1
            case "D":
                heady -= 1
        # move tail
        tailxs[0],tailys[0] = movetail(headx,heady,tailxs[0],tailys[0])
        for i in range(1,9):
            tailxs[i],tailys[i] = movetail(tailxs[i-1],tailys[i-1],tailxs[i],tailys[i])
        visited.add(str(tailxs[8]) + " " + str(tailys[8]))
print(len(visited))
