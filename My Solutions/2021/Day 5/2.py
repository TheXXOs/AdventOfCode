# begin opening code
with open("in.txt") as f:
    inp = f.read().split('\n')
# end opening code

# put daily code below here, copy this file for part 2
points = set()
double = set()
overlaps = 0
def raange(start,stop):
    if start <= stop:
        return range(start,stop+1)
    else:
        return range(start,stop-1,-1)
def checkfor(point):
    global points
    global double
    global overlaps
    if (point in points) and (point not in double):
        overlaps += 1
        double.add(point)
        #print(point+" *")
    else:
        #print(point)
        points.add(point)
for line in inp:
    #print(line)
    coords = line.split(" -> ")
    # check if horizontal or vertical
    start = coords[0].split(",")
    end = coords[1].split(",")
    if int(start[0]) == int(end[0]):
        for i in raange(int(start[1]),int(end[1])):
            point = start[0]+","+str(i)
            checkfor(point)
    elif int(start[1]) == int(end[1]):
        for i in raange(int(start[0]),int(end[0])):
            point = str(i)+","+start[1]
            checkfor(point)
    elif int(start[1]) < int(end[1]):
        j = int(start[1])
        for i in raange(int(start[0]),int(end[0])):
            point = str(i)+","+str(j)
            checkfor(point)
            j += 1
    else: # start[1] > end[1]
        j = int(start[1])
        for i in raange(int(start[0]),int(end[0])):
            point = str(i)+","+str(j)
            checkfor(point)
            j -= 1
    #print("=======")
print(overlaps)
# put daily code above here
