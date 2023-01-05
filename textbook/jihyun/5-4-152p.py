# 미로 찾기
from collections import deque

def BFS(maze, pos):
    queue = deque([pos])

    h, w = len(maze), len(maze[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # out of range
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            # monster
            if maze[nx][ny] == 0:
                continue

            # not visited
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

            # print(maze)

    print(maze[-1][-1])


def main():
    n, m = map(int, input().split())

    maze = []
    for i in range(n):
        maze.append(list(map(int, list(input()))))
    
    # print(maze)

    BFS(maze, (0, 0))

main()