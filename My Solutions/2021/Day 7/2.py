# begin opening code
with open("in.txt") as f:
    inp = f.read().split(',')
# end opening code
inp = [int(i) for i in inp]

# put daily code below here, copy this file for part 2
correct = 1000000000000000
for i in range(min(inp),max(inp)+1):
    total = 0
    for j in inp:
        n = abs(i-j)
        total += (n*(n+1))//2
    if total < correct:
        correct = total
print(correct)
# put daily code above here
