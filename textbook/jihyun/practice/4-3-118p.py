# 게임 개발

"""
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1

4 4
1 1 0
1 1 1 1 
1 0 0 1
1 0 0 1
1 1 1 1
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())

field = []
for i in range(n):
    field.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
field[x][y] -= 1

while True:
    for i in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        npos = field[nx][ny]

        if npos == 0:
            x, y = nx, ny
            field[nx][ny] -= 1
            print(f'({nx},{ny})')
            count += 1
            break
        else:
            d = nd

        if i == 3:
            nd = (d + 2) % 4
            x = x + dx[nd]
            y = y + dy[nd]

    if field[x][y] == 1:
        break

print(count)
print(field)