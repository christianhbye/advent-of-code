fname = "day7.txt"
with open(f"inputs/{fname}") as f:
    data = f.readlines()

op1 = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}
op2 = op1.copy()
op2["||"] = lambda x, y: int(str(x) + str(y))

def f(line):
    line = line.strip("\n")
    x, y = line.split(":")
    r = int(x)
    f = [int(i) for i in y.split()]
    return r, f

def valid(r, f, operators=op1):
    all_tot = {"+": f[0]}
    for fac in f[1:]:
        keys = list(all_tot.keys())
        for k in keys:
            v = all_tot.pop(k)
            for name, fcn in operators.items():
                tot = fcn(v, fac)
                if tot <= r:
                    key = k + name
                    all_tot[key] = tot
    return r in all_tot.values()

def calibration(operators=op1):
    cnt = 0
    for i, line in enumerate(data):
        res, fac = f(line)
        if valid(res, fac, operators=operators):
            cnt += res
    return cnt

# Part 1
print(calibration())
# Part 2
print(calibration(operators=op2))
