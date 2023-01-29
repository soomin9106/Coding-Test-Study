# 행성 터널
"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
https://www.acmicpc.net/problem/2887
"""
import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, v1, v2):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

n = int(input())
parent = [i for i in range(n + 1)]
positions = []
edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    positions.append((i + 1, x, y, z))

for i in range(1, 4):
    positions = sorted(positions, key=lambda x: x[i])
    # print(positions)
    for j in range(n - 1):
        w = abs(positions[j][i] - positions[j + 1][i])
        # print(w)
        
        edges.append((w, positions[j][0], positions[j + 1][0]))

edges.sort()

result = 0
for e in edges:
    cost, v1, v2 = e
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        result += cost

print(result)