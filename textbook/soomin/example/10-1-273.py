# 기본적인 서로소 집합 알고리즘 구현
import sys

sys.stdin = open("textbook/soomin/example/input.txt","rt")

# 최악의 경우 시간 복잡도: O(V)
def find_parent(parent, x):
    if parent[x] != x: # if not root node, do recursive finding process
        return find_parent(parent, parent[x])
    return x

def find_parent_optimize(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_optimize(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent_optimize(parent, a)
    b = find_parent_optimize(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


print('각 원소가 속한 집합:', end=' ')
for i in range(1, v+1):
    print(find_parent_optimize(parent, i), end=' ')
print()

print('부모 테이블 내용:', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()

