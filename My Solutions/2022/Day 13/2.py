import json
from functools import cmp_to_key
f = open("in.txt", "r")
file = f.read().splitlines()

def compare(a,b):
    if type(a) == int and type(b) == list:
        return compare([a],b)
    elif type(a) == list and type(b) == int:
        return compare(a,[b])
    elif type(a) == list and type(b) == list:
        for i in range(min([len(a),len(b)])):
            c = compare(a[i],b[i])
            if c != 0:
                return c
        if len(a) < len(b):
            return -1 # right order
        elif len(a) > len(b):
            return 1 # wrong order
        else:
            return 0 # no decision yet
    else:
        if a < b:
            return -1 # right order
        elif a > b:
            return 1 # wrong order
        else:
            return 0 # no decision yet

index = 0
total = 1
for line in sorted(([json.loads(x) for x in file if x != '']+[[[2]],[[6]]]),key=cmp_to_key(compare)):
    index += 1
    if line == [[2]] or line == [[6]]:
        total *= index
print(total)
