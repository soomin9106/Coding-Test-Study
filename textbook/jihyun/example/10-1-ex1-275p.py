# 서로소 집합 알고리즘
"""
6 4
1 4
2 3
2 4
5 6
"""

def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])

    return parent[v]

def union_parent(parent, v1, v2):
    v1 = find_parent(parent, v1)
    v2 = find_parent(parent, v2)

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

    return parent

def main():
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i

    for _ in range(e):
        v1, v2 = map(int, input().split())

        if find_parent(parent, v1) == find_parent(parent, v2):
            print('cycle 발생')
            
        parent = union_parent(parent, v1, v2)

    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print("\n부모 테이블: ", end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')

    print()

if __name__ == "__main__":
    main()