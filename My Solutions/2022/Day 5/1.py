import re
#i'm just hard-coding my input, don't mind me
crates = ["FCJPHTW","GRVFZJBH","HPTR","ZSNPHT","NVFZHJCD","PMGFWDZ","MVZWSJDP","NDS","DZSFM"]
f = open("in.txt", "r")
for line in f.read().split("\n"):
    nums = [int(s) for s in re.findall(r'\d+', line)]
    for i in range(nums[0]):
        crates[nums[2]-1] += crates[nums[1]-1][-1]
        crates[nums[1]-1] = crates[nums[1]-1][:-1]
for i in crates:
    print(i[-1],end="")
