import re
import numpy as np

with open("inputs/day6.txt") as fh:
    data = fh.readlines()


def g(line):
    return [int("".join(re.findall(r"(\d+)", line)))]


ts = g(data[0])
ds = g(data[1])


def root_diff(tt, d):
    disc = tt**2 - 4 * d
    return np.sqrt(disc)


def roots(tt, d):
    diff = root_diff(tt, d)
    r1 = tt / 2 - diff / 2
    r2 = tt / 2 + diff / 2
    return r1, r2


ans = 1
for tt, d in zip(ts, ds):
    r1, r2 = roots(tt, d)
    if np.allclose(r1, int(r1)):
        r1 += 1e-6
    if np.allclose(r2, int(r2)):
        r2 -= 1e-6
    diff = np.floor(r2) - np.ceil(r1) + 1
    print(diff)
    ans *= int(diff)
print(ans)
