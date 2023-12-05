import re

with open("inputs/day5.txt") as fh:
    data = fh.readlines()


def f(line):
    v = re.findall(r"(\d+)", line)
    return [int(vv) for vv in v]


def m(data, lstart, lstop, x):
    if lstop is None:
        lines = data[lstart:]
    else:
        lines = data[lstart:lstop]
    for l in lines:
        dest, source, r = f(l)
        smax = source + r - 1
        if (x >= source) and (x <= smax):
            return dest + (x - source)
    return x


xvals = f(data[0])
headers = [i for i, l in enumerate(data) if ":" in l]
headers = headers[1:]
for i, h in enumerate(headers):
    lstart = h + 1
    try:
        lstop = headers[i + 1] - 1
    except:
        lstop = None
    xvals = [m(data, lstart, lstop, x) for x in xvals]

print(xvals.index(min(xvals)))
print(min(xvals))


bg = xvals.index(min(xvals))
print(bg)  # even nr so beginning of a range
