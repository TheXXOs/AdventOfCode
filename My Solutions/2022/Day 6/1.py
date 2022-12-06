f = open("in.txt", "r")
a = ""
b = ""
c = ""
d = ""
incr = 0
for char in f.read().split("\n")[0]:
    if a and b and c and d and len({a,b,c,d}) == 4:
        print(a+b+c+d,"@",incr)
        break
    else:
        a = b
        b = c
        c = d
        d = char
        incr += 1
