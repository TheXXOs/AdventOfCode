import json
f = open("in.txt", "r")
file = f.read().split("\n\n")

def compare(a,b):
    if type(a) == int and type(b) == list:
        return compare([a],b)
    elif type(a) == list and type(b) == int:
        return compare(a,[b])
    elif type(a) == list and type(b) == list:
        for i in range(min([len(a),len(b)])):
            c = compare(a[i],b[i])
            if c != "both":
                return c
        if len(a) < len(b):
            return True # right order
        elif len(a) > len(b):
            return False # wrong order
        else:
            return "both" # no decision yet
    else:
        if a < b:
            return True # right order
        elif a > b:
            return False # wrong order
        else:
            return "both" # no decision yet
index = 0
total = 0
for line in file:
    pair = line.split("\n")
    for i in range(2):
        pair[i] = json.loads(pair[i])
    index += 1
    if compare(pair[0],pair[1]):
        total += index
print(total)
