import re
import time

with open("inputs/day5.txt") as fh:
    data = fh.readlines()


def f(line):
    v = re.findall(r"(\d+)", line)
    return [int(vv) for vv in v]


ss = f(data[0])[::2]
sr = f(data[0])[1::2]


def valid_seed(y):
    for i in range(len(ss)):
        start = ss[i]
        stop = start + sr[i]
        if (start <= y) and (y <= stop):
            return True
    return False


headers = [i for i, l in enumerate(data) if ":" in l]
headers = headers[1:]


def m(data, lstart, lstop, x):
    if lstop is None:
        lines = data[lstart:]
    else:
        lines = data[lstart:lstop]
    for line in lines:
        dest, source, r = f(line)
        smax = source + r - 1
        if (x >= source) and (x <= smax):
            return dest + (x - source)
    return x


def minv(data, lstart, lstop, y):
    if lstop is None:
        lines = data[lstart:]
    else:
        lines = data[lstart:lstop]
    for line in lines:
        d, s, r = f(line)
        dmax = d + r - 1
        if (y >= d) and (y <= dmax):
            return s + (y - d)
    return y


# upper limits
xvals = ss
for i, h in enumerate(headers):
    lstart = h + 1
    try:
        lstop = headers[i + 1] - 1
    except IndexError:
        lstop = None
    xvals = [m(data, lstart, lstop, x) for x in xvals]
upper = min(xvals)
print(upper, xvals.index(upper))

print(headers[::-1])
time.sleep(5)
j = 0

while True:
    if j % 100000:
        print(j, j / upper)
    yt = j
    if yt > upper:
        raise ValueError
    for i in range(len(headers)):
        lstart = headers[-(i + 1)] + 1
        if i == 0:
            lstop = None
        else:
            lstop = headers[-(i + 1) + 1] - 1
        #    print(lstart, lstop)
        yt = minv(data, lstart, lstop, yt)
    #   print(i, yt)
    if valid_seed(yt):
        print(yt)
        break
    else:
        j += 1

# forward run
xvals = [yt]
print(xvals)
print("start")
for i, h in enumerate(headers):
    lstart = h + 1
    try:
        lstop = headers[i + 1] - 1
    except IndexError:
        lstop = None
    xvals = [m(data, lstart, lstop, x) for x in xvals]
    print(i, xvals)
