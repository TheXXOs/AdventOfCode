f = open("in.txt", "r")
ma = 0
mb = 0
mc = 0
now = 0
for line in f.read().split("\n"):
    if line == "":
        if ma <= now:
            mc = mb
            mb = ma
            ma = now
        elif mb <= now:
            mc = mb
            mb = now
        elif mc <= now:
            mc = now
        now = 0
    else:
        now += int(line)
print(ma+mb+mc)
