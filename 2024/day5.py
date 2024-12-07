TEST = False
folder = "inputs"
if TEST:
    folder = folder + "_test"
fname = "day5.txt"
with open(f"{folder}/{fname}") as f:
    data = f.readlines()

def parse_rule(rule):
    rule = rule.strip("\n").split("|")
    return int(rule[0]), int(rule[1])

def parse_update(update):
    return [int(x) for x in update.strip("\n").split(",")]

def ordered(update, rules):
    for i in range(len(update)-1):
        rev_pair = (update[i+1], update[i])
        if rev_pair in rules:
            return False
    return True

s_ix = data.index("\n")
rules = [parse_rule(rule) for rule in data[:s_ix]]
updates = [parse_update(update) for update in data[s_ix+1:]]

s = 0
for up in updates:
    if ordered(up, rules):
        s += up[int(len(up)//2)]
print(s)

def order(update_old, rules):
    update = update_old.copy()
    fixed = 0
    for i in range(len(update)-1):
        rev_pair = (update[i+1], update[i])
        if rev_pair in rules:
            update[i], update[i+1] = rev_pair   # flip
            fixed += 1
    return update, fixed

s = 0
for up in updates:
    fixed = 1
    new_up = up
    its = 0
    while fixed > 0:
        new_up, fixed = order(new_up, rules)
        its += 1
    if its > 1:
        s += new_up[int(len(new_up)//2)]
print(s)
