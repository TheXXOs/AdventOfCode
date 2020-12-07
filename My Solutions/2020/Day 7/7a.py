#day 7
#i am at a friend's house rn, but it's not a big deal
#nope, jk, i did horribly. i hate recursion :D
#tysm flumble :)

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

bagRules = {}
for line in cList:
    lsplit = line.split()
    bagRule = lsplit[0]+" "+lsplit[1]
    bagCont = []
    numline = 0
    bagType = ""
    for spaced in lsplit[4:]:
        if (not spaced.isnumeric()) and (not spaced in ["bags,", "bags.", "bag,", "bag"]):
            bagType += spaced
            if numline % 2 == 0:
                bagType += " "
            else:
                if bagType != "no other":
                    bagCont.append(bagType)
                bagType = "" # made a dumb mistake here, had == instead of =
            numline += 1
    bagRules[bagRule] = bagCont
goldFound = 0
bagsHaveGold = []
def containsAShinyGoldBag(bag):
    for child in bagRules[bag]:
      if child == "shiny gold":
        return True
      elif containsAShinyGoldBag(child):
          return True
def doNothing():
    return
#def recursionSucks(lis, rootBag):
#    global bagRules
#    global goldFound
#    for bag in lis:
#        if "shiny gold" in bagRules[bag]:
#            if not rootBag in bagsHaveGold:
#                goldFound += 1
#                bagsHaveGold.append(rootBag)
#            return
#        elif bagRules[bag] == []:
#            doNothing()
#        else:
#            recursionSucks(bagRules[bag], rootBag)
for i in bagRules:
    if containsAShinyGoldBag(i):
        goldFound += 1
print(goldFound)
