# 플로이드

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
import sys

input = sys.stdin.readline
INF = int(1e9)

def solution(n, graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print("0", end=" ")
            else:
                print(graph[i][j], end=" ")
        
        print()

def main():
    n = int(input())
    m = int(input())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        v1, v2, w = map(int, input().split())
        graph[v1][v2] = min(graph[v1][v2], w)

    solution(n, graph)

if __name__ == "__main__":
    main()