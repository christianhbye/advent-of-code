with open("inputs/day1.txt") as f:
    data = f.read()

def add_digits(data):
    total = 0
    for d in data.split("\n")[:-1]:
        digits = [s for s in d if s.isdigit()]
        add = int("".join([digits[0], digits[-1]]))
        #print(digits, add)
        total += add
    print(total)

# part 1
add_digits(data)

# part 2
keys = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
for i in range(1, 10):
    dig = str(i)
    old = keys[dig]
    new = "".join([old[0], dig, old[-1]])
    data = data.replace(old, new)
add_digits(data)
