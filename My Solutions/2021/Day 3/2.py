# begin opening code
with open("in.txt") as f:
    inp = f.read().split('\n')
# end opening code

# put daily code below here, copy this file for part 2
def generate(inp,deg=0,out=""):
    inpp = list(inp)
    for j in range(len(inpp)):
        inpp[j] = inpp[j][deg:]
    if not inpp[0]:
        return out
    ones = 0
    total = len(inpp)
    for line in inpp:
        if line[0] == "1":
            ones+=1
    if ones >= total-ones:
        out += "1"
    else:
        out += "0"
    new = []
    for i in range(len(inpp)):
        if not((ones >= total-ones and inpp[i][0] == "0") or (ones < total-ones and inpp[i][0] == "1")):
            new.append(inpp[i])
    if len(new) == 1:
        out += new[0][1:]
        return out
    return generate(new,deg=1,out=out)

def generateCO(inp,deg=0,out=""):
    inpp = list(inp)
    for j in range(len(inpp)):
        inpp[j] = inpp[j][deg:]
    if not inpp[0]:
        return out
    ones = 0
    total = len(inpp)
    for line in inpp:
        if line[0] == "1":
            ones+=1
    if ones < total-ones:
        out += "1"
    else:
        out += "0"
    new = []
    for i in range(len(inpp)):
        if not((ones < total-ones and inpp[i][0] == "0") or (ones >= total-ones and inpp[i][0] == "1")):
            new.append(inpp[i])
    if len(new) == 1:
        out += new[0][1:]
        return out
    return generateCO(new,deg=1,out=out)
print(generate(inp))
print(generateCO(inp))
print("========")
print(int(generate(inp),base=2)*int(generateCO(inp),base=2))

# put daily code above here
