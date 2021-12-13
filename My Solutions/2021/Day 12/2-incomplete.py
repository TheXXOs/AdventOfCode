# copy this file for part 2

with open("in.txt") as f:
    inp = f.read().split('\n')
inp = [list(i.split("-")) for i in inp]

#with open("bugfix.txt") as f: # REMOVE
#    bug = f.read().split("\n") # REMOVE

for i in inp:
    if "end" in i:
        inp.remove(i)
        inp.append(i)
def getOther(val,tup):
    if tup.index(val) == 0:
        return tup[1]
    else:
        return tup[0]
#foundpaths = [] # REMOVE
count = 0
def findPaths(index, visited, once=False, path=["start"]):
    # index is str, visited is a set, once is bool
    global inp
    global count
    for i in inp:
        if index in i:
            j = getOther(index,i)
            if j == "end":
                count += 1
#                foundpaths.append(",".join(path)+",end") # REMOVE
                return None
            elif j not in visited:
                n = path + [j]
                if j.isupper():
                    k = visited
                    l = once
                    findPaths(j,k,l,n)
                else:
                    for m in [False,True]:
                        if m and not once: # if choose to visit once
                            k = visited
                            l = True
                        else:
                            k = visited.union({j})
                            l = once
                    findPaths(j,k,l,n)
findPaths("start",{"start"})
#for i in bug: # REMOVE
#    if i not in foundpaths: # REMOVE
#        print(i) # REMOVE
print(count)
