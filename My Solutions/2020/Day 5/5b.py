#day 5
#eyy im doing these quickly

f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()

seats = []
highestID = 0
for i in cList:
    upperLim = 127
    lowerLim = 0
    upperLimB = 7
    lowerLimB = 0
    for char in i[:7]:
        if char == "F":
            upperLim = lowerLim+int((upperLim-lowerLim)/2)
        elif char == "B":
            lowerLim = lowerLim+int((upperLim-lowerLim)/2)
    row = upperLim
    for char in i[7:]:
        if char == "L":
            upperLimB = lowerLimB+int((upperLimB-lowerLimB)/2)
        elif char == "R":
            lowerLimB = lowerLimB+int((upperLimB-lowerLimB)/2)
    column = upperLimB
    seatID = (row*8)+column
    seats.append(seatID)
for i in range(1024):
    if not i in seats and i <= 900 and i >= 100:
        print(i)
