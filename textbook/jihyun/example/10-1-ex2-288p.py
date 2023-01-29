# 크루스칼 알고리즘
"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""

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

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

edges = []
result = 0

for i in range(e):
    v1, v2, w = map(int, input().split())
    edges.append((w, v1, v2))

edges.sort()

for e in edges:
    cost, v1, v2 = e

    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)

        result += cost

print(result)