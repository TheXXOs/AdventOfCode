#day 3
#the fixed version of part 2
def countTrees(envList,dMove,rMove):
    treeCount = 0
    i = 0
    j = 0
    for line in envList:
        if j%dMove==0:
            if line[i%len(line)] == "#":
                treeCount += 1
            i += rMove
        j += 1
    return treeCount
f = open("input.txt", "r")
content = f.read()
cList = content.splitlines()
f.close()
# usage of countTrees()
# envList is the list of lines in the "environment"
# dMove is the number of steps to move down
# rMove is the number of steps to move right
print(countTrees(cList,1,1)*countTrees(cList,1,3)*countTrees(cList,1,5)*countTrees(cList,1,7)*countTrees(cList,2,1))
