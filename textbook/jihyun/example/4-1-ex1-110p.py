"""
5
R R R U D D
"""

n = int(input())
moves = input().split()

dx = {'R': 0, 'L': 0, 'U': -1, 'D': 1}
dy = {'R': 1, 'L': -1, 'U': 0, 'D': 0}

x, y = 1, 1

for move in moves:
    nx = x + dx[move]
    ny = y + dy[move]

    if nx <= 0 or ny <= 0 or nx > n or ny > n:
        continue
    
    x = nx
    y = ny
    # print(f'{move} -> ({x}, {y})')

# print()
print(x, y)  