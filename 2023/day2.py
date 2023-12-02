with open("inputs/day2.txt") as f:
    data = f.readlines()
R = 12
G = 13
B = 14
total = 0
for d in data:
    ids, s = d.split(":")
    s = s.replace("\n", "").split(";")
    _incnt = 0
    for se in s:
        cs = se.split(", ")
        _inincnt = 0
        for c in cs:
            if "blue" in c:
                if int(c[:-5]) <= B:
                    _inincnt += 1
            elif "green" in c:
                if int(c[:-6]) <= G:
                    _inincnt += 1
            elif "red" in c:
                if int(c[:-4]) <= R:
                    _inincnt += 1
        if _inincnt == len(cs):
            _incnt += 1
    if _incnt == len(s):
        total += int(ids[len("Game "):])
print(total)

total = 0
for d in data:
    ids, s = d.split(":")
    s = s.replace("\n", "").split(";")
    mb = 0
    mg = 0
    mr = 0
    for se in s:
        cs = se.split(", ")
        for c in cs:
            if "blue" in c:
                b = int(c[:-5])
                if b >= mb:
                    mb = b
            elif "green" in c:
                g = int(c[:-6])
                if g >= mg:
                    mg = g
            elif "red" in c:
                r = int(c[:-4])
                if r >= mr:
                    mr = r
    total += mb * mr * mg
print(total)
