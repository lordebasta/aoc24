from typing import List

with open('./input.txt') as f:
    reports = f.readlines()


def is_safe(report: List[int]):
    increasing = report[1] > report[0]
    for i in range(1, len(report)):
        if increasing and report[i] < report[i-1]:
            return False
        if not increasing and report[i] > report[i-1]:
            return False
        if not 1 <= abs(report[i] - report[i-1]) <= 3:
            return False
    return True


safe_cnt = 0
for report in reports:
    report = report.strip()
    report = report.split(' ')
    report = [int(x) for x in report]

    if is_safe(report):
        safe_cnt += 1

print(safe_cnt)
