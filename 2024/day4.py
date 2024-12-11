TEST = False
folder = "inputs"
if TEST:
    folder = folder + "_test"
fname = "day4.txt"
with open(f"{folder}/{fname}") as f:
    data = f.readlines()


def f(line, match="XMAS"):
    return line.count(match)


def cnt(d):
    return sum(f(line) for line in d)


def reverse(d):
    """
    Reverse row by row.
    """
    return [_d[::-1] for _d in d]


def transpose(d):
    dt = []
    for i in range(len(d[0])):
        dt.append("".join([line[i] for line in d]))
    return dt


def diag(d, pad):
    N = len(d)
    new_d = []
    for i, l in enumerate(d):
        if pad == "left":
            row = (N - i) * "0" + l + i * "0"
        elif pad == "right":
            row = i * "0" + l + (N - i) * "0"
        new_d.append(row)
    return transpose(new_d)


fwd = data
bwd = reverse(fwd)
dwn = transpose(data)
up = reverse(dwn)
dia_dr = diag(data, pad="right")  # down to right
dia_ul = reverse(dia_dr)  # up to left
dia_dl = diag(data, pad="left")  # down to left
dia_ur = reverse(dia_dl)  # up to right

s = 0
for d in [fwd, bwd, dwn, up, dia_dr, dia_ul, dia_dl, dia_ur]:
    s += cnt(d)
print(s)


# part 2
def cross_mas(d, line_num):
    if line_num == 0 or line_num == len(d) - 1:
        return 0
    above, line, below = d[line_num - 1 : line_num + 2]
    tot = 0
    for i, c in enumerate(line):
        if c == "A":
            r = above[i - 1] + c + below[i + 1]
            l = above[i + 1] + c + below[i - 1]
            if "MAS" in [r, r[::-1]] and "MAS" in [l, l[::-1]]:
                tot += 1
    return tot


print(sum(cross_mas(data, n) for n in range(len(data))))
