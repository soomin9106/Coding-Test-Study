# 위상 정렬
# 시간 복잡도 : O(V + E) [노드와 간선을 모두 확인]
import sys
from collections import deque, defaultdict

sys.stdin = open("textbook/soomin/example/input.txt","rt")

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = defaultdict(list)

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1 # 위상 줄이기

            if indegree[node] == 0: # 진입차수가 0이 되면 큐에 삽입
                q.append(node)
    
    for i in result:
        print(i, end=' ')
    print()

topology_sort()