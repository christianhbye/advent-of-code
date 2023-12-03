import re

with open("inputs/day3.txt") as fh:
    data = fh.readlines()


def f(line):
    ix = []
    for m in re.finditer(r"[\*]", line.replace("\n", "")):
        ix.append(m.start())
    return ix


syms = {}
for i, line in enumerate(data):
    syms[i] = f(line)

pns = []
for i, tries in syms.items():
    for t in tries:
        pnt = []
        for k in [-1, 0, 1]:
            added = []
            for p in [-1, 0, 1]:
                lv = i + k
                pv = t + p
                if lv < 0 or pv < 0 or lv > len(data) - 1 or pv > len(data[0]):
                    pass
                else:
                    for m in re.finditer(r"(\d+)", data[lv]):
                        if m.group() in added:
                            pass
                        elif m.start() <= pv and m.end() - 1 >= pv:
                            added.append(m.group())
                            val = int(data[lv][m.start() : m.end()])
                            pnt.append(val)
        if len(pnt) == 2:
            pns.append(pnt[0] * pnt[1])
print(sum(pns))
