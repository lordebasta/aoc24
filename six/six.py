from collections import defaultdict


with open("test", "r") as file:
    mat = file.readlines()

m = len(mat)
for i in range(m):
    mat[i] = list(mat[i].strip())
n = len(mat[0])

pos = None
for r in range(m):
    for c in range(n):
        if mat[r][c] == '^':
            pos = [r, c]
            break

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
diri = 0

dir_mat = defaultdict(set)


def creates_loop(r, c, diri):
    diri = (diri+1) % len(dirs)
    while 0 <= r < m and 0 <= c < n:
        x, y = dirs[diri]
        r, c = pos


while 0 <= pos[0] < m and 0 <= pos[1] < n:
    x, y = dirs[diri]
    r, c = pos

    if 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] != "#":
        if creates_loop(r, c, diri):
            print((r, c))
        i = 1
        a, b = dirs[]
        while True:
            delta_r, delta_c = a*i, b*i
            if not 0 <= r+delta_r < m or not 0 <= c+delta_c < n or \
               mat[r+delta_r][c+delta_c] == "#":
                break

            if mat[r+delta_r][c+delta_c] == "X" and (a, b) in dir_mat[(r+delta_r, c+delta_c)]:
                print(r, c)
                break

            longr, longc = r+a*(i+1), c+b*(i+1)
            if 0 <= longr < m and 0 <= longc < n and \
               mat[longr][longc] == "#":

            i += 1

    while 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] == "#":
        diri = (diri + 1) % len(dirs)
        x, y = dirs[diri]

    dir_mat[(r, c)].add((x, y))
    mat[r][c] = "X"
    pos = [r+x, c+y]
    if 0 <= r+x < m and 0 <= c+y < n:
        mat[r+x][c+y] = "^"

a = 0
for l in mat:
    a += l.count('X')
print(a)
