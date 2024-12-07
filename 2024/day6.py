fname = "day6.txt"
TEST = False
if TEST:
    path = f"inputs_test/{fname}"
else:
    path = f"inputs/{fname}"

with open(path) as f:
    data = [list(line.strip("\n")) for line in f.readlines()]

class Guard:

    pos = []
    Npos = 0
    d = 1j

    def __init__(self, data=data):
        self.data = {}
        for y, line in enumerate(data[::-1]):  # y increases upwards
            for x, c in enumerate(line):
                self.data[x + y * 1j] = c
        self.find_start()

    def find_start(self):
        for k, v in self.data.items():
            if v == "^":
                self.pos.append(k)
                self.Npos += 1
                return

    def move(self):
        p = self.pos[-1] + self.d
        if not p in self.data:
            return False
        c = self.data[p]
        if c == ".":
            self.data[p] = "X"
            self.pos.append(p)
            self.Npos += 1
        elif c == "X":
            self.pos.append(p)
        elif c == "#":
            self.d *= -1j
        return True

g = Guard()
print(g.pos)
while g.move():
    print(g.pos[-1], g.Npos)
print(g.Npos)
