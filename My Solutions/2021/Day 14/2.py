# copy this file for part 2
import collections as cl
with open("in.txt") as f:
    inp = f.read().split('\n')
# inp = [int(i) for i in inp]

pol = inp[0]
inp = dict([i.split(" -> ") for i in inp[2:]])
counts = dict.fromkeys(inp,0)
for j in range(len(pol)-1):
    counts[pol[j]+pol[j+1]] += 1

for _ in range(40):
    newcounts = dict.fromkeys(inp,0)
    for i in counts:
        newcounts[i[0]+inp[i]] += counts[i]
        newcounts[inp[i]+i[1]] += counts[i]
    counts = dict(newcounts)

letters = {}
for i in counts:
    if i[0] in letters:
        letters[i[0]] += counts[i]
    else:
        letters[i[0]] = counts[i]
letters[pol[-1]] += 1
print(letters[max(letters,key=lambda k: letters[k])]-letters[min(letters,key=lambda k: letters[k])])
