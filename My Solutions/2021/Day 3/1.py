# begin opening code
with open("in.txt") as f:
    inp = f.read().split('\n')
# end opening code

# put daily code below here, copy this file for part 2
ones = []
for i in range(len(inp[0])):
    ones.append(0)
total = 0
for line in inp:
    total += 1
    for char in range(len(line)):
        if line[char] == "1":
            ones[char] +=1
gamma = ""
epilson = ""
for i in ones:
    if i >= total - i:
        gamma += "1"
        epilson += "0"
    else:
        gamma += "0"
        epilson += "1"
print(int(gamma,base=2)*int(epilson,base=2))
# put daily code above here
