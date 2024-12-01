fname = "day1.txt"
with open(f"inputs/{fname}") as f:
    data = f.readlines()


def f(line):
    x, y = line.strip("\n").split(" ")
    return x, y


list1 = []
list2 = []
for i, line in enumerate(data):
    x, y = f(line)
    list1.append(x)
    list2.append(y)
