# 인구 이동
"""
2 20 50
50 30
20 40
--> 1

2 40 50
50 30
20 40
--> 0

2 20 50
50 30
30 40
--> 1

3 5 10
10 15 20
20 30 25
40 22 10
--> 2

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
--> 3
"""
from collections import deque

def solution(arr, low, high, st):
    n = len(arr)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([st])
    visited = [[False] * n for _ in range(n)]
    union = set()

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        # print(f"x: {x}  y: {y}")
        # union = []

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
            
            # 이웃한 나라의 인구 수 차이가 범위 안일 때
            if low <= abs(arr[x][y] - arr[nx][ny]) <= high:
                # print(f"nx: {nx}  ny: {ny}")
                # print(list(queue))
                union.add((x, y))
                union.add((nx, ny))
                
    if not union:
        return False
    
    sum = 0
    for x, y in union:
        sum += arr[x][y]
    
    mean = sum // len(union)
    print(f"union: {union}")
    print(f"sum: {sum} len: {len(union)}")
    for x, y in union:
        arr[x][y] = mean
    
    return True


n, low, high = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ct = 0
while solution(arr, low, high, (0, 0)):
    print(arr)
    ct += 1

print(ct)