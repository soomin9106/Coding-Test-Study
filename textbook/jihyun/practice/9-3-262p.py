# 전보
"""
3 2 1
1 2 4
1 3 2
"""

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def solution(n, graph, distance, st):
    pq = []

    heapq.heappush(pq, (0, st))
    distance[st] = 0
        
    while pq:
        dist, cur = heapq.heappop(pq)

        for i in graph[cur]:
            if distance[i[1]] < dist:
                continue
            
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(pq, (cost, i[1]))

    ct = 0
    max_val = 0
    for i in distance[1:]:
        if i != INF:
            ct += 1
            max_val = max(max_val, i)

    return ct - 1, max_val

def main():
    n, m, st = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(m):
        v1, v2, w = map(int, input().split())
        graph[v1].append((w, v2))

    print(solution(n, graph, distance, st))

if __name__ == "__main__":
    main()