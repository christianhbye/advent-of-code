import re

with open("inputs/day3.txt") as fh:
    data = fh.readlines()


def f(line):
    ix = []
    for m in re.finditer(r"[^.0-9]", line.replace("\n", "")):
        ix.append(m.start())
    return ix


def g(line):
    ix = []
    for m in re.finditer(r"(\d+)", line.replace("\n", "")):
        ix.append([m.start(), m.end()])
    return ix


# def g(line):
#    return re.findall(r"(\d+)", line.replace("\n", ""))

# part 1
nums = {}
syms = {}
for i, line in enumerate(data):
    nums[i] = g(line)
    syms[i] = f(line)

pns = []
L = len(pns)
for i, tries in nums.items():
    if i == 0:
        checks = syms[i] + syms[i + 1]
    elif i == len(data) - 1:
        checks = syms[i - 1] + syms[i]
    else:
        checks = syms[i - 1] + syms[i] + syms[i + 1]
    for t in tries:
        c = True
        for j in range(t[0], t[1]):
            for k in [-1, 0, 1]:
                if (j + k) in checks:
                    v = data[i][t[0] : t[1]]
                    print(v)
                    pns.append(int(v))
                    c = False
                    break
                else:
                    continue
            if not c:
                break


print(sum(pns))
