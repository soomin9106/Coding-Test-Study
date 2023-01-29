# 위상정렬
"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
from collections import deque

def topology_sort(v, graph, indegree):
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=" ")
    
    print()

def main():
    v, e = map(int, input().split())

    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        indegree[v2] += 1

    topology_sort(v, graph, indegree)

main()