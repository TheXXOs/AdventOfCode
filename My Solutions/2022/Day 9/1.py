f = open("in.txt", "r")
headx = 0
heady = 0
tailx = 0
taily = 0
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
        if heady != taily and headx != tailx and (abs(heady-taily) >= 2 or abs(headx-tailx) >= 2):
            taily += int((heady-taily)/abs(heady-taily))
            tailx += int((headx-tailx)/abs(headx-tailx))
        elif abs(heady-taily) >= 2:
            taily += int((heady-taily)/abs(heady-taily))
        elif abs(headx-tailx) >= 2:
            tailx += int((headx-tailx)/abs(headx-tailx))
        visited.add(str(tailx) + " " + str(taily))
print(len(visited))
