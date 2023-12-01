import numpy as np

sums = []
with open("inputs/day1.txt") as f:
    data = f.read().split("\n\n")[:-1]
    for i, d in enumerate(data):
        sums.append(np.sum(np.array(d.split("\n")).astype(int)))

sums = np.sort(sums)
print(sums[-1])
print(np.sum(sums[-3:]))
