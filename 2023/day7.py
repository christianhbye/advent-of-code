fname = "day7.txt"
with open(f"inputs/{fname}") as fh:
    data = fh.readlines()

m = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for i in range(1, 10):
    m[str(i)] = i


def f(line, m):
    hand, b = line.strip("\n").split(" ")
    hand = [m[h] for h in hand]
    return hand, int(b)


def wild_cnt(hand):
    njs = hand.count(1)
    if njs == 5:
        return [5]
    mix = -1
    mcnt = 0
    i = 0
    c = []
    huse = hand[njs:]
    while i < len(huse):
        cnt = huse.count(huse[i])
        if cnt > mcnt:
            mcnt = cnt
            mix = i
        c.append(cnt)
        i += cnt
    c[mix] += njs
    return c


def score(hand, wild=False):
    if wild and 1 in hand:
        c = wild_cnt(hand)
    else:
        i = 0
        c = []
        while i < len(hand):
            cnt = hand.count(hand[i])
            c.append(cnt)
            i += cnt
    if 5 in c:
        return 7
    elif 4 in c:
        return 6
    elif 3 in c:
        if 2 in c:
            return 5
        else:
            return 4
    else:
        return 6 - len(c)


def tb(hand):
    return sum([h * 15**i for i, h in enumerate(hand[::-1])]) / 15 ** len(
        hand
    )


def winnings(m, pt2=False):
    scores = []
    bets = []
    for i, line in enumerate(data):
        h, b = f(line, m)
        s = score(sorted(h), wild=pt2) + tb(h)
        scores.append(s)
        bets.append(b)

    bets_sorted = [b for _, b in sorted(zip(scores, bets))]
    return sum([b * (i + 1) for i, b in enumerate(bets_sorted)])


# pt 1
print(winnings(m))

# pt 2
m["J"] = 1
print(winnings(m, pt2=True))
