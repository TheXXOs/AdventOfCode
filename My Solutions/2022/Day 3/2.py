f = open("in.txt", "r")
def ord2(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38
total = 0
text = f.read().split("\n")
lines = [text[i:i+3] for i in range(0,len(text), 3)]
for lineg in lines:
    brk = False
    for a in lineg[0]:
        for b in lineg[1]:
            for c in lineg[2]:
                if a == b and b == c:
                    total += ord2(a)
                    brk = True
                    break
            if brk:
                break
        if brk:
            break
print(total)
