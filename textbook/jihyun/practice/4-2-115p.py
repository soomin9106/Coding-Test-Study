# 왕실의 나이트

start = input()

x = int(start[1])
y = ord(start[0]) - ord('a') + 1

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

count = 0
for i in range(8):
    nx = dx[i] + x
    ny = dy[i] + y

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count += 1

print(count)