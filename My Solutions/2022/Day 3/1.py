f = open("in.txt", "r")
def ord2(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38
total = 0
for line in f.read().split("\n"):
    brk = False
    rucka = line[slice(0,len(line)//2)]
    ruckb = line[slice(len(line)//2,len(line))]
    for char in rucka:
        for chbr in ruckb:
            if char == chbr:
                total += ord2(char)
                brk = True
                break
        if brk:
            break
print(total)
