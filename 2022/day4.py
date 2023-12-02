with open("inputs/day4.txt") as f:
    data = f.readlines()

total = 0
for d in data:
    d = d.replace("\n", "")
    ns = [s.split("-") for s in d.split(",")]
    cmin = int(ns[0][0]) <= int(ns[1][0])
    cmax = int(ns[0][1]) >= int(ns[1][1])
    ncmin = int(ns[0][0]) >= int(ns[1][0])
    ncmax = int(ns[0][1]) <= int(ns[1][1])
    if cmin and cmax or ncmin and ncmax:
        total += 1
print(total)

total = 0
for d in data:
    d = d.replace("\n", "")
    ns = [s.split("-") for s in d.split(",")]
    c1 = int(ns[0][1]) >= int(ns[1][0])
    c2 = int(ns[0][0]) <= int(ns[1][1])
    if c1 and c2:
        total += 1
print(total)
