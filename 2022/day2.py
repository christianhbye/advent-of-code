import numpy as np

with open("inputs/day2.txt") as f:
    data = f.read().split("\n")[:-1]

ok = {"A": 1, "B": 2, "C": 3}
mk = {"X": 1, "Y": 2, "Z": 3}
col1 = []  # opponent
col2 = []  # me
result = []
for d in data:
    opp = ok[d[0]]
    me = mk[d[-1]]
    col1.append(opp)
    col2.append(me)
    if opp == me:
        result.append(3)
    elif (me - opp) % 3 == 1:
        result.append(6)
    else:
        result.append(0)
total_score = np.sum(col2) + np.sum(result)
print(total_score)

# part 2
res_score = (np.array(col2) - 1) * 3  # result in column 2 now
shape_score = []
for o, r in zip(col1, col2):
    my_shape = (o + r) % 3 + 1
    shape_score.append(my_shape)
print(np.sum(res_score) + np.sum(shape_score))
