# 게임 개발

import sys

sys.stdin = open("imple/input.txt","rt")

n, m = map(int, input().split())

visit = [[0] * m for _ in range(n)] # 방문 기록 
x, y, direction = map(int, input().split())

# 실제 지도
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visit[x][y] = 1 # 첫번째 노드는 방문 처리

# 북, 동, 남, 서 순서대로
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

count = 1
turn_time = 0
while True:
    turn_left() # 왼쪽 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visit[nx][ny] == 0 and arr[nx][ny] == 0: # 방문 하지도 않았고, 육지인 경우
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1 # 방문
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        # 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else: # 가능하지 않으면 멈추기
            break
        turn_time = 0


print(count)


