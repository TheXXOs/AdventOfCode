# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split('\n')
# inp = [int(i) for i in inp]
start = "0,0"
end = str(len(inp[0])-1)+","+str(len(inp)-1)
visited = {}
current = [""]
nxt = {start:[start,0]} # {node:[path,dist]}
while end != current[0]:
    current = min(nxt.items(),key=lambda x: x[1][1]) # current is ('x,y', ['path', dist])
    visited[current[0]] = current[1]
    nxt.pop(current[0])
    # make NODES here; node is {"x,y":dist}
    a = current[0].split(",")
    nodes = {}
    if int(a[0]) < len(inp[0])-1:
        nodes[str(int(a[0])+1)+","+a[1]] = int(inp[int(a[1])][int(a[0])+1])
    if int(a[1]) < len(inp)-1:
        nodes[a[0]+","+str(int(a[1])+1)] = int(inp[int(a[1])+1][int(a[0])])
    # end making NODES
    for node in nodes: # dict of connections
        if node not in visited:
            if node in nxt:
                if nxt[node][1] > current[1][1]+nodes[node]:
                        nxt[node] = [current[1][0]+"-"+node, current[1][1]+nodes[node]]
            else:
                nxt[node] = [current[1][0]+"-"+node, current[1][1]+nodes[node]]
print(current[1][1])
