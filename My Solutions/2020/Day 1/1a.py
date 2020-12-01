# AoC Day One
# The server has crashed but we know the challenge
# Find 2 numbers that add to 2020 in a list
# And output the product
f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
testinga = 0
for i in cList:
    testingb = 0
    for j in cList:
        if not (testinga == testingb):
            if int(i)+int(j) == 2020:
                print(int(i)*int(j))
        testingb += 1
    testinga += 1
