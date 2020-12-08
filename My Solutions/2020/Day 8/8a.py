#day 8
#late by a bit, i probably should make my alarm sooner.

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

acc = 0
currentInst = 0
instDone = []
noLoopYet = True
while noLoopYet:
    if currentInst in instDone:
        print(acc)
        break
    if cList[currentInst][:3] == "acc":
        instDone.append(currentInst)
        if cList[currentInst][4] == "-":
            acc -= int(cList[currentInst][5:])
        else:
            acc += int(cList[currentInst][5:])
        currentInst += 1
    elif cList[currentInst][:3] == "nop":
        instDone.append(currentInst)
        currentInst += 1
    else:
        instDone.append(currentInst)
        if cList[currentInst][4] == "-":
            currentInst -= int(cList[currentInst][5:])
        else:
            currentInst += int(cList[currentInst][5:])
