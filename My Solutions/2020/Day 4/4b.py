#day 4
#aaa im late again
f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
unchecked = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
    "cid": True}
validPass = 0
passChecked = dict(unchecked)

validHCL = ["0","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
validECL = ["amb","blu","brn","gry","grn","hzl","oth"]

def checkForValid(ppt):
    global validPass
    global validHCL
    global validECL
    checked = 0
    for key in ppt:
        if key == "byr":
            if int(ppt[key]) >= 1920 and int(ppt[key]) <= 2002:
                checked += 1
        elif key == "iyr":
            if int(ppt[key]) >= 2010 and int(ppt[key]) <= 2020:
                checked += 1
        elif key == "eyr":
            if int(ppt[key]) >= 2020 and int(ppt[key]) <= 2030:
                checked += 1
        elif key == "hgt":
            if ppt[key][-2:] == "cm":
                if int(ppt[key][:-2]) >= 150 and int(ppt[key][:-2]) <= 193:
                    checked += 1
            elif ppt[key][-2:] == "in":
                if int(ppt[key][:-2]) >= 59 and int(ppt[key][:-2]) <= 76:
                    checked += 1
        elif key == "hcl":
            if ppt[key][0] == "#":
                hlccheck = 0
                for j in ppt[key][1:]:
                    if j in validHCL:
                        hlccheck += 1
                if hlccheck == 6:
                    checked += 1
        elif key == "ecl":
            if ppt[key] in validECL:
                checked += 1
        elif key == "pid":
            if ppt[key].isnumeric() and len(ppt[key]) == 9:
                checked += 1
        elif key == "cid":
            checked += 1
    if checked == 8:
        validPass += 1

for line in cList:
    if line == "": # do this if new passport
        checked = 0
        for key in passChecked:
            if passChecked[key]:
                checked += 1
        if checked == 8:
            checkForValid(passChecked)
        passChecked = dict(unchecked)
    else: # do this if not new passport
        dList = line.split()
        for i in dList:
            passChecked[i[:3]] = i[4:]
checked = 0
for key in passChecked:
    if passChecked[key]:
        checked += 1
if checked == 8:
    checkForValid(passChecked)
print(validPass)
