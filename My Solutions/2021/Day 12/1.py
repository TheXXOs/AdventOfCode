# copy this file for part 2
# 1. Create a recursive function that takes index of node of a graph and the destination index.
#    Keep a global or a static variable count to store the count.
#    Keep a record of the nodes visited in the current path by passing a visited array by value
#    (instead of reference, which would not be limited to the current path).

# 2. If the current nodes is the destination increase the count.

# 3. Else for all the adjacent nodes, i.e. nodes that are accessible from the current node,
#    call the recursive function with the index of adjacent node and the destination.

# 4. Print the Count.

with open("in.txt") as f:
    inp = f.read().split('\n')
inp = [list(i.split("-")) for i in inp]
for i in inp:
    if "end" in i:
        inp.remove(i)
        inp.append(i)
def getOther(val,tup):
    if tup.index(val) == 0:
        return tup[1]
    else:
        return tup[0]

count = 0
def findPaths(index, visited): # index is str, visited is a set
    global inp
    global count
    for i in inp:
        if index in i:
            j = getOther(index,i)
            if j == "end":
                count += 1
                return None
            elif j not in visited:
                if j.isupper():
                    k = visited
                else:
                    k = visited.union({j})
                findPaths(j,k)
findPaths("start",{"start"})
print(count)
