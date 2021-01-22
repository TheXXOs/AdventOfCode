#day 14
#hopefully this isn't too hard?

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
        value = f'{int(i[1]):036b}'
        final = ""
        for (n,char) in enumerate(value):
            if mask[n] == "0":
                final += char
            else:
                final += mask[n]
        mem[i[0]] = final
total = 0
for x in mem:
    subtotal = 0
    xtimes = mem[x].count("X")
    xtimes = 2**xtimes
    for y in range(xtimes):
        for (n,char) in enumerate(mem[x]):
            if char != "X":
                subtotal += (2**(36-n))*int(char)
            elif y%2 == 0:
                subtotal += (2**(36-n))
    total += subtotal
print(total)
