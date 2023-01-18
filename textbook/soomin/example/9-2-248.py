# 개선된 다익스트라 알고리즘 코드
# heapq 사용
# 시간 복잡도: O(ELogV)

import sys 
from collections import defaultdict
import heapq

INF = int(1e9)

sys.stdin = open("textbook/soomin/example/input.txt","rt")

# 노드 개수, 간선 개수
n, m = map(int, input().split())

start = int(input())

graph = defaultdict(list)
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    # node a to b, cost c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 실행
def dijkstra(start):
    # heapq 정의 
    q = []
    # 처음 노드 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        # 최단 노드에 대한 정보 
        dist, now = heapq.heappop(q)

        # 처리 된 적 있다면 pass
        if dist > distance[now]:
            continue

        # 인접 노드 searching
        for j in graph[now]:
            cost = dist + j[1]

            if cost < distance[j[0]]: # update case
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])
