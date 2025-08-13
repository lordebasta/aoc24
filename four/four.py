if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for i, l in enumerate(lines):
        lines[i] = list(l.strip())
        print(lines[i])

    word = "XMAS"
    m, n = len(lines), len(lines[0])
    moves = ((x, y) for x in range(-1, 2) for y in range(-1, 2))
    moves = list(moves)
    print(moves)

    def f(r, c, i, x, y):
        if r < 0 or c < 0 or r == m or c == n:
            return 0
        if lines[r][c] != word[i]:
            return 0
        if i == 3:
            print(r, c, i, lines[r][c])
            return 1

        if x is None:
            print(r, c, i, lines[r][c])
            res = 0
            for lx, ly in moves:
                print(lx,ly)
                res += f(r+lx, c+ly, i+1, lx, ly)
            print("end", res)
            return res
        if x is not None:
            print("\t", r, c, i, x, y, lines[r][c])
            return f(r+x, c+y, i+1, x, y)

        return 0

    res = 0
    for r in range(m):
        for c in range(n):
            if lines[r][c] == "X":
                res += f(r, c, 0, None, None)

    print(res)
