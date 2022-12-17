# very slow and also i don't know if it'll get to the right answer or not so

f = open("in.txt", "r")
file = f.read().splitlines()[0]

def canmove(chamber,rock,rockpos,direction="V"):
    if direction == "V": # move down
        rockpos = (rockpos[0],rockpos[1]+1)
    elif direction == "<": # move left
        if rockpos[0] == 0: # at wall
            return False
        rockpos = (rockpos[0]-1,rockpos[1])
    elif direction == ">":
        if rockpos[0]+len(rock[0]) >= 7: # at wall
            return False
        rockpos = (rockpos[0]+1,rockpos[1])
    for row in range(len(rock)):
        r = len(chamber)-1-row-rockpos[1]
        for col in range(len(rock[row])):
            c = col + rockpos[0]
            if rock[row][col] == "#" and chamber[r][c] == "#":
                return False
    return True

chamber = ["#######"]
rocks = [["####"],
         [".#.","###",".#."],
         ["..#","..#","###"],
         ["#","#","#","#"],
         ["##","##"]]
floors = [0,0,0,0,0,0,0]
saved = 0

jetnum = 0
for i in range(1000000000000):
    if i%10000 == 0:
        print(int(i/10000),"/",100000000)
    chamber = chamber + [".......",".......","......."]
    currentrock = rocks[i%5]
    chamber = chamber + ["......." for i in range(len(currentrock))]
    rockpos = (2,0)
    falling = True
    while falling:
        # jet of gas
        if canmove(chamber,currentrock,rockpos,direction=file[jetnum]):
            if file[jetnum] == "<":
                rockpos = (rockpos[0]-1,rockpos[1])
            else:
                rockpos = (rockpos[0]+1,rockpos[1])
        jetnum += 1
        jetnum %= len(file)
        # fall
        try:
            if canmove(chamber,currentrock,rockpos):
                rockpos = (rockpos[0],rockpos[1]+1)
            else:
                falling = False
        except IndexError:
            falling = False
    # add to chamber
    for row in range(len(currentrock)):
        r = len(chamber)-1-row-rockpos[1]
        for col in range(len(currentrock[row])):
            c = col + rockpos[0]
            if currentrock[row][col] != ".":
                chamber[r] = chamber[r][:c] + "#" + chamber[r][c+1:]
    # update distance to floors
    updated = [False,False,False,False,False,False,False]
    for row in range(len(chamber)-1,-1,-1):
        for j in range(7):
            if chamber[row][j] == "#" and not updated[j]:
                floors[j] = row
                updated[j] = True
        if all(updated):
            break
    ab = len(chamber)
    chamber = chamber[min(floors):]
    saved += ab-len(chamber)
    # remove air rows
    chamber = list(filter(lambda a: a != ".......", chamber))
print(len(chamber)+saved-1)
