f = open("in.txt", "r")
file = f.read().splitlines()
nextcomm = ""
wait = 0
counter = 0
x = 1
step = 0
line = ""
while counter != len(file)+1:
    step += 1
    if wait == 0:
        if counter != len(file):
            nextcomm = file[counter]
        counter += 1
        match nextcomm.split(" ")[0]:
            case "noop":
                wait = 1
            case "addx":
                wait = 2
    wait -= 1
    #print here!!!
    if step%40 == 1:
        print()
    if abs(((step-1)%40)-(x%40)) <= 1:
        print("█",end="")
    else:
        print(" ",end="")
    if wait == 0:
        cmd = nextcomm.split(" ")
        if cmd[0] == "addx":
            x += int(cmd[1])
