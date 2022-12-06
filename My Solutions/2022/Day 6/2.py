f = open("in.txt", "r")
search = [""] * 14
incr = 0
for char in f.read().split("\n")[0]:
    if (not "" in search) and len(set(search)) == 14:
        print(search,"@",incr)
        break
    else:
        search.pop(0)
        search.append(char)
        incr += 1
