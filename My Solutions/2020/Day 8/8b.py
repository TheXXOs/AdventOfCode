#day 8
#late by a bit, i probably should make my alarm sooner.

f = open("input.txt", "r")
content = f.read()
cListt = content.splitlines()
f.close()

def myFunc(cList, findAcc):
    acc = 0
    currentInst = 0
    instDone = []
    noLoopYet = True
    while noLoopYet:
        if currentInst in instDone:
            if findAcc:
                return acc
            else:
                return False
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
        if currentInst >= (len(cList)-1):
            if findAcc:
                return acc
            else:
                return True
j = 0
for i in cListt:
    if i[:3] != "acc":
        cLista = list(cListt)
        if i[:3] == "nop":
            cLista[j] = "jmp" + cListt[j][3:]
        elif i[:3] == "jmp":
            cLista[j] = "nop" + cListt[j][3:]
        if myFunc(cLista, False):
            print(myFunc(cLista,True))
    j += 1 # this was initially 1 tab too far in; i didn't see it
