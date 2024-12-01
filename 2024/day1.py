fname = "day1.txt"
with open(f"inputs/{fname}") as f:
    data = f.readlines()


def f(line):
    r = line.strip("\n").split(" ")
    x, y = r[0], r[-1]
    return x, y


list1 = []
list2 = []
for i, line in enumerate(data):
    x, y = f(line)
    list1.append(int(x))
    list2.append(int(y))

list1.sort()
list2.sort()

# pt 1
distances = [abs(x - y) for x, y in zip(list1, list2)]
print(sum(distances))

# pt 2
sim_score = 0
for i in list1:
    sim_score += i * list2.count(i)
print(sim_score)
