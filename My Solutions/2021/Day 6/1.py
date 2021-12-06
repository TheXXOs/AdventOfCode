# begin opening code
with open("in.txt") as f:
    inp = list(map(int, f.read().split(',')))
# end opening code

# put daily code below here, copy this file for part 2
days = 80
for i in range(days):
    for j in range(len(inp)):
        if inp[j] == 0:
            inp[j] = 6
            inp.append(8)
        else:
            inp[j]-=1
print(len(inp))

# put daily code above here
