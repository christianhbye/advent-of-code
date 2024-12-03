fname = "day2.txt"
with open(f"inputs/{fname}") as f:
    data = f.readlines()


def f(line):
    nums = [int(x) for x in line.strip("\n").split(" ")]
    return nums


def safe(nums):
    s = nums[1] - nums[0]
    for i in range(len(nums) - 1):
        d = nums[i + 1] - nums[i]
        if d * s < 0:
            return False
        if abs(d) < 1:
            return False
        if abs(d) > 3:
            return False
    return True


cnt = 0
cnt2 = 0
for i, line in enumerate(data):
    nums = f(line)
    if safe(nums):
        cnt += 1
    else:
        for j in range(len(nums)):
            _ncpy = nums.copy()
            del _ncpy[j]
            if safe(_ncpy):
                cnt2 += 1
                break

print(cnt)
print(cnt + cnt2)
