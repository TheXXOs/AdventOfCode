# begin opening code
with open("in.txt") as f:
    inp = f.read().split('\n')
# end opening code

# put daily code below here, copy this file for part 2
def raange(start,stop):
    if start <= stop:
        return range(start,stop+1)
    else:
        return range(start,stop-1,-1)

points = []
double = []
overlaps = 0
for line in inp:
    coords = line.split(" -> ")
    # check if horizontal or vertical
    start = coords[0].split(",")
    end = coords[1].split(",")
    '''if start == end:
        point = start[0]+","+start[1]
        if (point in points) and (point not in double):
            overlaps += 1
            double.append(point)
            #print(point)
        else:
            points.append(point)'''
    if start[0] == end[0]:
        for i in raange(int(start[1]),int(end[1])):
            point = start[0]+","+str(i)
            #print(point)
            if (point in points) and (point not in double):
                overlaps += 1
                double.append(point)
                #print(point)
            else:
                points.append(point)
    elif start[1] == end[1]:
        for i in raange(int(start[0]),int(end[0])):
            point = str(i)+","+start[1]
            #print(point)
            if (point in points) and (point not in double):
                overlaps += 1
                double.append(point)
                #print(point)
            else:
                points.append(point)
    #print("======")
    # check if any point has already been
print(overlaps)
# put daily code above here
