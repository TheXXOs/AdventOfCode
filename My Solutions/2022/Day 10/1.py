f = open("in.txt", "r")
file = f.read().splitlines()
nextcomm = ""
wait = 0
counter = 0
x = 1
step = 0
total = 0
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
    if step%40 == 20:
        total += x*step
        print(step,x,x*step)
    wait -= 1
    if wait == 0:
        cmd = nextcomm.split(" ")
        if cmd[0] == "addx":
            x += int(cmd[1])
print(total)
