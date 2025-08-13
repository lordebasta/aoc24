from collections import Counter


if __name__ == "__main__":
    with open('input2.txt', 'r') as file:
        lines = file.readlines()

    for i, l in enumerate(lines):
        lines[i] = list(l.strip())
        print(lines[i])

    print(lines)
    m, n = len(lines), len(lines[0])

    res = 0

    def isx(r, c):
        def isMAS(c):
            return c == Counter(["M", "S"])

        ax, ay, bx, by = -1, -1, 1, 1
        cnt = Counter()
        cnt[lines[r+ax][c+ay]] += 1
        cnt[lines[r+bx][c+by]] += 1
        if not isMAS(cnt): return False

        ax, ay, bx, by = -1, 1, 1, -1
        cnt = Counter()
        cnt[lines[r+ax][c+ay]] += 1
        cnt[lines[r+bx][c+by]] += 1
        if not isMAS(cnt): return False

        return True

    for r in range(1, m-1):
        for c in range(1, n-1):
            if lines[r][c] == "A":
                res += int(isx(r, c))

    print(res)
