f = open("in.txt", "r")
count = 0
for line in f.read().split("\n"):
    lspl = line.split(",")
    grpa = lspl[0].split("-")
    grpb = lspl[1].split("-")
    if ((int(grpa[0]) <= int(grpb[1]) and int(grpa[0]) >= int(grpb[0])) or (int(grpa[1]) <= int(grpb[1]) and int(grpa[1]) >= int(grpb[0]))) or ((int(grpb[0]) <= int(grpa[1]) and int(grpb[0]) >= int(grpa[0])) or (int(grpb[1]) <= int(grpa[1]) and int(grpb[1]) >= int(grpa[0]))):
        # unnecessarily-long if statements!!! yay!!!!!
        count += 1
print(count)
