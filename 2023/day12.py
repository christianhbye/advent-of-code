fname = "day12.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.read().split("\n")

def proc(line):
    p, n = line.split()
    ns = [int(i) for i in n.split(",")]
    return p, ns

def valid(pattern, ns):
    ndots = len(pattern) - sum(ns)
    if pattern.count(".") > ndots:
        return False
    p = pattern.replace("?", ".")
    groups = [g for g in p.split(".") if len(g)]
    for i, g in enumerate(groups):
        if g.count("#") > ns[i]:
            return False
    return True

def f(pattern, ns):
    pos = pattern.find("?")  # first ?
    if pos == -1:
        return []
    pdot = pattern.replace("?", ".", 1)
    phash = pattern.replace("?", "#", 1)
    returns = []
    for p in [pdot, phash]:
        if valid(p, ns):
            returns.append(p)
    return returns

n_orders = 0
for line in data[:1]:
    pattern, ns = proc(line)
    patterns = [pattern]
    cont = True
    while cont:
        newpatterns = []
        cnt = 0
        for p in patterns:
            np = f(p, ns)
            if np == []:
                cnt += 1
                np = p
            newpatterns.extend(np)
        patterns = newpatterns
        count = cnt < len(patterns)

print(patterns)
