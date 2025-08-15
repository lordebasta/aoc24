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

dir_mat = dict()

while 0 <= pos[0] < m and 0 <= pos[1] < n:
    x, y = dirs[diri]
    r, c = pos
    dir_mat[(r, c)] = (x, y)

    if 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] != "#":
        a, b = dirs[(diri+1) % len(dirs)]
        if mat[r+a][c+b] == "X" and (a, b) == dir_mat[(r+a, c+b)]:
            print(r, c)

    while 0 <= r+x < m and 0 <= c+y < n and mat[r+x][c+y] == "#":
        diri = (diri + 1) % len(dirs)
        x, y = dirs[diri]

    mat[r][c] = "X"
    pos = [r+x, c+y]
    if 0 <= r+x < m and 0 <= c+y < n:
        mat[r+x][c+y] = "^"

a = 0
for l in mat:
    a += l.count('X')
print(a)
