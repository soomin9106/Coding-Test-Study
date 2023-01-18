# 전보
# 다익스트라 알고리즘 

import sys
from collections import defaultdict
import heapq

sys.stdin = open("textbook/soomin/practice/input.txt","rt")

INF = int(1e9)

n, m, c = map(int, input().split())
graph = defaultdict(list)
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


start = c
q = []

distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

count = 0
max_dist = 0

for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)


print(count - 1, max_dist)