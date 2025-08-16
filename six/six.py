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

res = [0]

def creates_loop(r, c, diri):
    ogr, ogc = r, c
    diri = (diri+1) % len(dirs)
    visited = set()
    while 0 <= r < m and 0 <= c < n:
        x, y = dirs[diri]

        while 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] == "#":
            diri = (diri + 1) % len(dirs)
            x, y = dirs[diri]

        if (x, y) in dir_mat[(r, c)]:
            print(f"start: ${(ogr, ogc)}, meet: ${(r, c)}")
            res[0] += 1
            break
        if (r, c) in visited:
            print(ogr, ogc)
            break
        visited.add((r, c))

        r += x
        c += y


while 0 <= pos[0] < m and 0 <= pos[1] < n:
    x, y = dirs[diri]
    r, c = pos

    if 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] != "#":
        creates_loop(r, c, diri)

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
print(res)
