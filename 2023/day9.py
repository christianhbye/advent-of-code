from functools import partial
import re

fname = "day9.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.readlines()


data = [[int(i) for i in re.findall(r"(-?\d+)", line)] for line in data]


def diff(line):
    d = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    return d


def xp(line, reverse=False):
    if reverse:
        d = line[::-1]
    else:
        d = line
    c = 0
    while d != [0] * len(d):
        c += d[-1]
        d = diff(d)
    return c


print(sum(map(xp, data)))
print(sum(map(partial(xp, reverse=True), data)))
