# 커리큘럼
# 위상 정렬
import sys
import copy
from collections import deque, defaultdict

sys.stdin = open("textbook/soomin/practice/input.txt","rt")

n = int(input())

indegree = [0] * (n+1)
graph = defaultdict(list)
time = [0] * (n+1) # 강의 시간

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])

topology_sort()
