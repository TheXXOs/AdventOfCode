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
for line in cList:
    if line == "": # do this if new passport
        checked = 0
        for key in passChecked:
            if passChecked[key]:
                checked += 1
        if checked == 8:
            validPass += 1
        passChecked = dict(unchecked)
    else: # do this if not new passport
        dList = line.split()
        for i in dList:
            passChecked[i[:3]] = True
checked = 0
for key in passChecked:
    if passChecked[key]:
        checked += 1
if checked == 8:
    validPass += 1
print(validPass)
