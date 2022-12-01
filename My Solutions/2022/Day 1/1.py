f = open("in.txt", "r")
mx = 0
now = 0
for line in f.read().split("\n"):
    if line == "":
        if mx < now:
            mx = now
        now = 0
    else:
        now += int(line)
print(mx)
