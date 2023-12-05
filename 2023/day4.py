import re

with open("inputs/day4.txt") as fh:
    data = fh.readlines()


def g(line):
    la, lb = line.split(":")
    l1, l2 = lb.split("|")
    wns = re.findall(r"(\d+)", l1)
    mine = [i for i in re.findall(r"(\d+)", l2) if i in wns]
    return mine


def f(line):
    mine = g(line)
    n = len(mine) - 1
    if n < 0:
        return 0
    return 2**n


print(sum(map(f, data)))


# p2
cards = {}
for i, d in enumerate(data):
    cards[i] = 1

for i, d in enumerate(data):
    nn = len(g(d))
    for j in range(nn):
        try:
            cards[i + j + 1] += cards[i]
        except KeyError:
            pass

print(sum(cards.values()))
