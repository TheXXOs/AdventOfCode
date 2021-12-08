# copy this file for part 2
with open("in.txt") as f:
    inp = f.read().split("\n")
# inp = [int(i) for i in inp]
total = 0
fig = {}
for i in inp:
    x = i.split(" | ")
    outs = x[1].split(" ")
    ins = x[0].split(" ")
    for j in ins:
        if len(j) == 2:
            fig["1"] = j
        elif len(j) == 3:
            fig["7"] = j
        elif len(j) == 4:
            fig["4"] = j
        elif len(j) == 7:
            fig["8"] = j
    for j in ins:
        if len(j) == 6:
            if set(fig["4"]).union(set(j)) == set("abcdefg"):
                if set(fig["1"]).union(set(j)) == set("abcdefg"):
                    fig["6"] = j
                else:
                    fig["0"] = j
            else:
                fig["9"] = j
    for j in ins:
        if len(j) == 5:
            if set(fig["1"]).union(set(j)) == set(fig["9"]):
                fig["5"] = j
            else:
                if set(fig["7"]).union(set(j)) == set(j):
                    fig["3"] = j
                else:
                    fig["2"] = j

    current = ""
    for j in outs:
        for k in fig:
            if set(j) == set(fig[k]):
                current += k
    if current:
        total += int(current)
print(total)
