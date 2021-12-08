# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split("\n")
# inp = [int(i) for i in inp]

total = 0
for i in inp:
    outs = i.split(" | ")[1].split(" ")
    print(outs)
    for j in outs:
        if len(j) in {2,3,4,7}:
            total += 1
print(total)
