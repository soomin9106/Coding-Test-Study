# 다익스트라 알고리즘

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""

import sys
import heapq
from time import time

input = sys.stdin.readline
INF = int(1e9)

def get_smallest_node(graph, visited, distance):
    n = len(graph) - 1
    min_val = INF
    min_idx = 0

    for i in range(1, n + 1):
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            min_idx = i
    
    return min_idx

def simple_dijkstra(start, graph, visited, distance):
    n = len(graph) - 1
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        cur = get_smallest_node(graph, visited, distance)
        visited[cur] = True

        for j in graph[cur]:
            cost = distance[cur] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    return distance[1:]

def heapq_dijkstra(start, graph, distance):
    n = len(graph) - 1
    hq = []
    
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, cur = heapq.heappop(hq)

        # 이미 방문한 노드는 건너뜀.
        if distance[cur] < dist:
            continue

        for i in graph[cur]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

    return distance[1:]


def main():
    v, e = map(int, input().split())
    start = int(input())

    graph = [[] for i in range(v + 1)]
    visited = [False] * (v + 1)
    distance = [INF] * (v + 1)

    for _ in range(e):
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2, w))

    st = time()
    print(simple_dijkstra(start, graph, visited, distance))
    print(f"simple: {time() - st} sec")

    st = time()
    print(heapq_dijkstra(start, graph, distance))
    print(f"heap queue: {time() - st} sec")

if __name__ == "__main__":
    main()
