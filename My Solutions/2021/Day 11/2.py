# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
inp = [list(i) for i in inp]
for i in range(len(inp)):
    for j in range(len(inp[i])):
        inp[i][j] = int(inp[i][j])
eight = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for i in range(1000):
    for j in range(10):
        for k in range(10):
            inp[j][k] += 1
            if inp[j][k] > 9:
                inp[j][k] = "X"
    while any("X" in subl for subl in inp):
        for j in range(10):
            for k in range(10):
                if inp[j][k] == "X":
                    for n in eight:
                        try:
                            if 0 <= j+n[0] < 10 and 0 <= k+n[1] < 10:
                                inp[j+n[0]][k+n[1]] += 1
                                if inp[j+n[0]][k+n[1]] > 9:
                                    inp[j+n[0]][k+n[1]] = "X" # x means highlighted but hasn't flashed
                        except:
                            pass
                    inp[j][k] = "█" # y means highlighted and has flashed
    simult = True
    for j in range(10):
        for k in range(10):
            if inp[j][k] != "█":
                simult = False
    if simult:
        print(i+1)
        break
    for j in range(10):
        for k in range(10):
            if inp[j][k] == "█":
                inp[j][k] = 0
