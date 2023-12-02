with open("inputs/day3.txt") as f:
    data = f.readlines()


def value(inp):
    sets = [set(i) for i in inp]
    c = "".join(sets[0].intersection(*sets[1:]))
    val = ord(c)
    if val <= ord("Z"):
        val += 27 - ord("A")
    else:
        val += 1 - ord("a")
    return val


total = 0
for d in data:
    N = int(len(d) // 2)
    s1, s2 = d[:N], d[N:]
    total += value((s1, s2))
print(total)

total = 0
i = 0
while i < len(data):
    inp = [data[i + j].replace("\n", "") for j in range(3)]
    total += value(inp)
    i += 3
print(total)
