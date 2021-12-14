# copy this file for part 2
import collections as cl
with open("in.txt") as f:
    inp = f.read().split('\n')
# inp = [int(i) for i in inp]
pol = inp[0]
inp = inp[2:]
for i in range(10):
    newpol = ""
    for j in range(len(pol)-1):
        newpol += pol[j]
        for k in inp:
            rule = k.split(" -> ")
            if pol[j]+pol[j+1] == rule[0]:
                newpol += rule[1]
    newpol += pol[-1]
    pol = str(newpol)
pc = cl.Counter(pol).most_common()
print(pc[0][1] - pc[-1][1])
