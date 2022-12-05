f = open("in.txt", "r")
count = 0
for line in f.read().split("\n"):
    lspl = line.split(",")
    grpa = lspl[0].split("-")
    grpb = lspl[1].split("-")
    if (int(grpa[0]) >= int(grpb[0]) and int(grpa[1]) <= int(grpb[1])) or (int(grpa[0]) <= int(grpb[0]) and int(grpa[1]) >= int(grpb[1])):
        count += 1
print(count)
