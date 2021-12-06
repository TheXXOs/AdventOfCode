# begin opening code
with open("in.txt") as f:
    inp = list(map(int, f.read().split(',')))
# end opening code

# put daily code below here, copy this file for part 2
days = 256
timers = [0,0,0,0,0,0,0,0,0]
for i in inp:
    timers[int(i)] += 1
for i in range(days):
    new = [0,0,0,0,0,0,0,0,0]
    new[8] += timers[0]
    new[6] += timers[0]
    for i in range(8):
        new[i] += timers[i+1]
    timers = list(new)
total = 0
for i in timers:
    total += i
print(total)

# put daily code above here
