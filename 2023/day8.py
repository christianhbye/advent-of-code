from math import lcm

fname = "day8.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.readlines()

pm = {"L": 0, "R": 1}
path = [pm[i] for i in data[0].strip("\n")]


def f(line):
    pos, tup = line.split("=")
    l, r = tup.split(",")
    return pos.strip(), l.strip()[1:], r.strip()[:-1]


d = data[2:]
m = {}

for line in d:
    pos, left, right = f(line)
    m[pos] = (left, right)

chain = ["AAA"]
p = "AAA"
while p != "ZZZ":
    lr = path[len(chain) % len(path) - 1]
    p = m[p][lr]
    chain.append(p)

# pt 1
print(len(chain) - 1)

# pt 2
walkers = [code for code in m if code[-1] == "A"]
steps = [0] * len(walkers)
for i, w in enumerate(walkers):
    s = steps[i]
    while w[-1] != "Z":
        lr = path[s % len(path)]
        w = m[w][lr]
        s += 1
    steps[i] = s
print(steps)
print(lcm(*steps))
