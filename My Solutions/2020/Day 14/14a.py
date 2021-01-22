#day 14
#new day, new *stressing that i won't ctach up in time*

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
cLList = []
for line in cList:
    ll = line.split(" = ")
    cLList.append(ll)
mem = {}
mask = ""
for i in cLList:
    if i[0] == "mask":
        mask = i[1]
    else:
        value = f'{int(i[1]):036b}' # woah weird formatting string
        final = ""
        for (n,char) in enumerate(value):
            if mask[n] == "X":
                final += char
            else:
                final += mask[n]
        mem[i[0]] = int(final,2)
total = 0
for x in mem:
    total += mem[x]
print(total)
