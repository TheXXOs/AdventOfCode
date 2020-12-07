#day 7
#hopefully i do better here

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

bagRules = {}
for line in cList:
    lsplit = line.split()
    bagRule = lsplit[0]+" "+lsplit[1]
    bagCont = []
    numline = 1
    bagType = ""
    for spaced in lsplit[4:]:
        if (not spaced in ["bags,", "bags.", "bag,", "bag"]):
            if spaced.isnumeric():
                bagNum = spaced
            else:
                bagType += spaced
            if numline % 3 == 2:
                bagType += " "
            elif numline % 3 == 0:
                if bagType != "no other":
                    bagCont.append([bagType,bagNum])
                bagType = "" # made a dumb mistake here, had == instead of =
            numline += 1
    bagRules[bagRule] = bagCont
biG = 0
def bagInGold(bag):
    global bagRules
    global biG
    if not bagRules[bag] == []:
        for i in bagRules[bag]:
            biG += int(i[1])
            for j in range(int(i[1])):
                bagInGold(i[0])
                
bagInGold("shiny gold")
print(biG)
