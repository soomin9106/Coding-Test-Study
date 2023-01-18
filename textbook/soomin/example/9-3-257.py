# 플로이드 워셜 알고리즘
# 시간 복잡도: O(N^3)
import sys

INF = int(1e9)

sys.stdin = open("textbook/soomin/example/input.txt","rt")

# 노드 개수, 간선 개수
n = int(input())
m = int(input())

# 2차원 리스트 만들기
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신은 0 으로 초기화
for i in range(1, n+1):
     for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('Infinity', end=' ')
        else:
            print(graph[a][b], end=" ")