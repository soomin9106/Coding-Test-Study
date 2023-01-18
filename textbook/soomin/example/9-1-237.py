# 간단한 다익스트라 알고리즘 구현
# 시간 복잡도: O(V^2)
import sys 
from collections import defaultdict

# input = sys.stdin.readlines
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

# 비용이 가장 작은 노드 인덱스 반환
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘 실행
def dijkstra(start):
    # 처음 노드 초기화
    distance[start] = 0
    visited[start] = 0

    # 인접 노드 거리 업데이트
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 방문하지 않은 곳에서 가장 비용이 작은 노드를 찾아서 
    # 인접한 노드의 cost 업데이트
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])