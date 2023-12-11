fname = "day11.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.read().split("\n")


def f(line):
    return [x for x in range(len(line)) if line[x] == "#"]


def g(data):
    galaxies = []
    allx = []
    ally = []
    for y, line in enumerate(data):
        xs = f(line)
        if not len(xs):
            continue
        if y not in ally:
            ally.append(y)
        for x in xs:
            if x not in allx:
                allx.append(x)
            galaxies.append((x, y))
    return galaxies, allx, ally


galaxies, allx, ally = g(data)
nox = [x for x in range(len(data[0])) if x not in allx]
noy = [y for y in range(len(data)) if y not in ally]


def expand(galaxies, nox, noy, pt2=False):
    galc = galaxies.copy()
    for i, g in enumerate(galc):
        x, y = g
        if not pt2:
            factor = 1
        else:
            factor = int(1e6) - 1
        x += factor * len([_x for _x in nox if _x < x])
        y += factor * len([_y for _y in noy if _y < y])
        galc[i] = (x, y)
    return galc


galaxies1 = expand(galaxies, nox, noy)


def distance(g1, g2):
    x1, y1 = g1
    x2, y2 = g2
    return abs(x2 - x1) + abs(y2 - y1)


def total_dist(galaxies):
    tot = 0
    for i in range(len(galaxies)):
        g1 = galaxies[i]
        j = 0
        while j < i:
            g2 = galaxies[j]
            dist = distance(g1, g2)
            tot += dist
            j += 1
    return tot


print(total_dist(galaxies1))
galaxies2 = expand(galaxies, nox, noy, pt2=True)
print(total_dist(galaxies2))
