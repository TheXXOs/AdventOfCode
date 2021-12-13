# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
    index = inp.index('')
    coords = set(inp[:index])
    folds = [i[11:].split("=") for i in inp[index+1:]]
for i in folds:
    newc = set()
    if i[0] == "x":
        # fold along x
        for j in coords:
            x = int(j.split(",")[0])
            fold = int(i[1])
            if x > fold:
                x = (2*fold)-x
            newc.add(str(x)+","+j.split(",")[1])
    else:
        # fold along y
        for j in coords:
            x = int(j.split(",")[1])
            fold = int(i[1])
            if x > fold:
                x = (2*fold)-x
            newc.add(j.split(",")[0]+","+str(x))
    coords = set(list(newc))
for i in range(len(inp[0])):
    line = ""
    for j in range(len(inp)):
        if str(j)+","+str(i) in coords:
            line += "█"
        else:
            line += "⠀"
        if j > 50:
            break
    if i > 30:
        break
    print(line)
