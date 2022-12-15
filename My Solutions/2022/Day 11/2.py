# my items
items = [[53, 89, 62, 57, 74, 51, 83, 97],
         [85, 94, 97, 92, 56],
         [86, 82, 82],
         [94, 68],
         [83, 62, 74, 58, 96, 68, 85],
         [50, 68, 95, 82],
         [75],
         [92, 52, 85, 89, 68, 82]]
inspections = [0,0,0,0,0,0,0,0]
opers = [lambda a : a*3,
         lambda a : a+2,
         lambda a : a+1,
         lambda a : a+5,
         lambda a : a+4,
         lambda a : a+8,
         lambda a : a*7,
         lambda a : a*a]
condits = [[1,5], # true, false
           [5,2],
           [3,4],
           [7,6],
           [3,6],
           [2,4],
           [7,0],
           [0,1]]
tests = [lambda a : a%13 == 0,
         lambda a : a%19 == 0,
         lambda a : a%11 == 0,
         lambda a : a%17 == 0,
         lambda a : a%3 == 0,
         lambda a : a%7 == 0,
         lambda a : a%5 == 0,
         lambda a : a%2 == 0]

# test items
'''items = [[79, 98],
         [54, 65, 75, 74],
         [79, 60, 97],
         [74]]
newitems = [[],[],[],[]]
inspections = [0,0,0,0]
opers = [lambda a : a*19,
         lambda a : a+6,
         lambda a : a*a,
         lambda a : a+3]
condits = [[2,3], # true, false
           [2,0],
           [1,3],
           [0,1]]
tests = [lambda a : a%23 == 0,
         lambda a : a%19 == 0,
         lambda a : a%13 == 0,
         lambda a : a%17 == 0]'''

for i in range(10000):
    for monkey in range(len(items)):
        for item in items[monkey]:
            item = opers[monkey](item)
            inspections[monkey] += 1
            item = item % 9699690 # stop numbers from growing uncontrollably without losing info
            if tests[monkey](item):
                items[condits[monkey][0]].append(item)
            else:
                items[condits[monkey][1]].append(item)
            items[monkey] = []
largest = max(inspections)
inspections.remove(largest)
second = max(inspections)
print(largest*second)
