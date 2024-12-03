fname = "day3.txt"
with open(f"inputs/{fname}") as f:
    data = f.readlines()

TEST = False
if TEST:
    data = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n"
    ]


def f(line, do=None):
    cnt = 0
    line = line.strip("\n")
    l = line.split("mul")
    i = -1
    for chunk in l:
        i += 1
        if not len(chunk):
            continue
        if do is not None:
            current_do = do
            if "do()" in chunk:
                if "don't()" in chunk.split("do()")[-1]:
                    do = False
                do = True
            elif "don't()" in chunk:
                do = False
            if not current_do:
                continue
        if chunk[0] != "(":
            continue
        if ")" not in chunk:
            continue
        if "," not in chunk:
            continue
        t = chunk[1:].split(")")[0].split(",")
        if len(t) != 2:
            continue
        try:
            prod = int(t[0]) * int(t[1])
        except ValueError:
            prod = 0
        cnt += prod
    if do is None:
        return cnt
    return cnt, do


s = 0
for line in data:
    s += f(line)
print(s)

s = 0
do = True
for line in data:
    _s, do = f(line, do=do)
    s += _s
print(s)
