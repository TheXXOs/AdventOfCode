f = open("in.txt", "r")
# part a - input to """tree"""
dirs = {}
currentnav = []
reading = False
usedspace = 0
for line in f.read().splitlines():
    if line[0] == "$": # command
        if reading:
            reading = False
        if line[2:4] == "cd": # change line
            if line[5:] == "..": # nav out
                currentnav.pop()
            else: # nav in
                currentnav.append(line[5:])
        elif line[2:4] == "ls": # list items
            dirs[" ".join(currentnav)] = []
            reading = " ".join(currentnav)
    elif reading:
        dirs[" ".join(currentnav)].append(line)
        if line.split(" ")[0] != "dir":
            usedspace += int(line.split(" ")[0])

# part b - remove dirs
subbing = True
while subbing:
    subbing = False
    for dire in dirs:
        for file in dirs[dire]:
            if file[:3] == "dir":
                subbing = True
                try:
                    for fil in dirs[dire + " " + file[4:]]:
                        dirs[dire].append(" ".join(fil.split(" ")[:-1] + [file[4:]] + fil.split(" ")[-1:]))
                except:
                    pass
                dirs[dire].remove(file)

# part c - calculate sizes
dsizes = {}
for dire in dirs:
    rtot = 0
    for file in dirs[dire]:
        rtot += int(file.split(" ")[0])
    dsizes[dire] = rtot

# part d - get answer
unused = 70000000 - usedspace
record = 70000000
for dire in dsizes:
    if dsizes[dire] < record and unused + dsizes[dire] > 30000000:
        record = dsizes[dire]

print(dire, record)
