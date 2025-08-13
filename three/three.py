import re

if __name__ == "__main__":
    with open("input.txt", "r") as input:
        input = input.read()

    matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input)

    res = 0
    for m in matches:
        nums = re.findall(r'[0-9]{1,3}', m)
        nums = list(map(int, nums))
        res += nums[0] * nums[1]

    print(res)

    enabled = True
    res = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input)
    for a, b, do, dont in matches:
        if do or dont:
            enabled = bool(do)
            continue
        if not enabled:
            continue
        res += int(a)*int(b)

    print(res)
