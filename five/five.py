import re

orders = []
updates = []
reading_orders = True

with open('input.txt', 'r') as file:
    for line in file.read().split('\n'):

        if not line:
            reading_orders = False
            continue

        if reading_orders:
            (a, b) = re.findall(r'(\d+)\|(\d+)', line)[0]
            orders.append((int(a), int(b)))
        else:
            nums = line.split(',')
            nums = list(map(int, nums))
            updates.append(nums)

print(orders)
print(updates)


def isnumokay(i, update):
    num = update[i]
    for num2 in update[:i]:
        for a, b in orders:
            if b == num2 and a == num:
                return False
    return True


def isupdatecorrect(update):
    for i in range(1, len(update)):
        if not isnumokay(i, update):
            return False
    return True


res = 0
incorrects = []
for update in updates:
    if not isupdatecorrect(update):
        incorrects.append(update)
        continue
    res += update[len(update)//2]

print(res)
print(incorrects)

rules = set()
for a, b in orders:
    rules.add((a, b))

for incorrect in incorrects:
    while not isupdatecorrect(incorrect):
        for i in range(len(incorrect)):
            for j in range(i+1, len(incorrect)):
                if (incorrect[j], incorrect[i]) in rules:
                    incorrect[j], incorrect[i] = incorrect[i], incorrect[j]

print(incorrects)

res = 0
for i in incorrects:
    mid = len(i) // 2
    res += i[mid]

print(res)
    
