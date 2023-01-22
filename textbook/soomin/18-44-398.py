# 행성 터널
# 크루스칼 알고리즘, 최소 신장 트리 찾기
# cost 구하는 방식에 대한 생각
# https://www.acmicpc.net/problem/2887

import sys

sys.stdin = open("textbook/soomin/input.txt","rt")

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
x_points = []
y_points = []
z_points = []
parent = [0] * (n + 1)

for i in range(1, n+1):
    x, y, z = map(int, input().split())
    x_points.append((x, i))
    y_points.append((y, i))
    z_points.append((z, i))

x_points.sort()
y_points.sort()
z_points.sort()

for i in range(1, n+1):
    parent[i] = i

edges = []
res = 0


for i in range(n-1):
    edges.append((x_points[i+1][0]- x_points[i][0], x_points[i][1], x_points[i+1][1]))
    edges.append((y_points[i+1][0]- y_points[i][0], y_points[i][1], y_points[i+1][1]))
    edges.append((z_points[i+1][0]- z_points[i][0], z_points[i][1], z_points[i+1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)