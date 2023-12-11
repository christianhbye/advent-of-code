fname = "day10.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.readlines()

pipes = {
    "|": ("s", "n"),
    "-": ("e", "w"),
    "L": ("n", "e"),
    "J": ("n", "w"),
    "7": ("s", "w"),
    "F": ("s", "e"),
}

all_pipes = {}


def td(pipe, fd):
    return [d for d in pipes[pipe] if d != fd][0]


def nextpipe(data, pos, all_pipes):
    x, y = pos
    pipe, fromdir = all_pipes[pos]
    todir = td(pipe, fromdir)
    if todir == "s":
        newx = x
        newy = y + 1
        newfdir = "n"
    elif todir == "n":
        newx = x
        newy = y - 1
        newfdir = "s"
    elif todir == "e":
        newx = x + 1
        newy = y
        newfdir = "w"
    else:
        newx = x - 1
        newy = y
        newfdir = "e"
    newpos = (newx, newy)
    if newpos in all_pipes:
        print("DONE")
        print(len(all_pipes), len(all_pipes) // 2)
        return False, newpos
    else:
        all_pipes[newpos] = (data[newy][newx], newfdir)
        return True, newpos


for i, line in enumerate(data):
    v = line.find("S")
    if v > 0:
        spos = (v, i)
        break

# XXX
for dx in [-1, 1]:
    if dx < 0:
        fd = "e"
    else:
        fd = "w"
    p = data[spos[1]][spos[0] + dx]
    if p in pipes:
        all_pipes[spos] = ("7", fd)

cont = True
pos = spos
while cont:
    cont, pos = nextpipe(data, pos, all_pipes)


area = 0
for y, line in enumerate(data):
    edgecnt = 0
    halfvert = []
    s = []
    line = line.strip("\n")
    for x in range(len(line)):
        pos = (x, y)
        if pos in all_pipes:
            p, fd = all_pipes[pos]
            s.append(p)
            if p == "|":
                edgecnt += 1
            elif p == "-":
                continue
            else:
                if fd in ["n", "s"]:
                    halfvert.append(fd)
                else:
                    tod = td(p, fd)
                    halfvert.append(tod)
                if len(halfvert) == 1:
                    continue
                elif len(halfvert) == 2:
                    if halfvert.count(halfvert[0]) == 1:
                        edgecnt += 1
                    halfvert = []
                else:
                    raise ValueError
                # print(halfvert)

        elif edgecnt % 2 == 1:
            s.append("I")
            area += 1
        else:
            s.append("O")
    print("".join(s))
print(area)
