fname = "day6.txt"
TEST = False
if TEST:
    path = f"inputs_test/{fname}"
else:
    path = f"inputs/{fname}"


def read_input(path):
    with open(path) as f:
        data = [list(line.strip("\n")) for line in f.readlines()]
    return data


DATA = read_input(path)


class Guard:
    def __init__(self, data=DATA):
        self.pos = []
        self.Npos = 0
        self.data = {}
        for y, line in enumerate(data[::-1]):  # y increases upwards
            for x, c in enumerate(line):
                self.data[x + y * 1j] = c
        self.find_start()

    def find_start(self):
        for k, v in self.data.items():
            if v == "^":
                self.data[k] = "X"
                self.pos.append((k, 1j))
                self.Npos += 1
                return

    def move(self, part=1, verbose=False):
        p = sum(self.pos[-1])
        try:
            c = self.data[p]
        except KeyError:
            return 0
        if c == ".":
            self.data[p] = "X"
            self.pos.append((p, self.pos[-1][1]))
            self.Npos += 1
        elif c == "X":
            cp = (p, self.pos[-1][1])
            self.pos.append(cp)
            if part == 2 and cp in self.pos[:-1]:
                return 2
        elif c == "#":
            pos = self.pos[-1]
            cp = (pos[0], pos[1] * -1j)
            self.pos.append(cp)
            if part == 2 and cp in self.pos[:-1]:
                return 2
        return 1


print("Part 1\n------")
g = Guard()
while g.move():
    pass
print(g.Npos)

# pt 2
print("Part 2\n------")
N = len(DATA)
M = len(DATA[0])
n_obs = 0
s = []
for i in range(N):
    for j in range(M):
        if i % 10 == 0 and j == 0:
            print(f"{i}/{N} {j}/{M}, {n_obs=}")
        d = read_input(path)
        if d[i][j] in ["#", "^"]:
            continue
        d[i][j] = "#"
        g = Guard(data=d)
        r = 1
        while r == 1:
            r = g.move(part=2)
        if r == 2:
            n_obs += 1
            s.append((i, j))
        del g
        del d
print(n_obs)
