# 플로이드 워셜 알고리즘

"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
import sys

input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall(v, graph):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            for k in range(1, v + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    return [g[1:] for g in graph[1:]]


def main():
    v = int(input())
    e = int(input())

    graph = [[INF] * (v + 1) for i in range(v + 1)]

    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i == j:
                graph[i][j] = 0

    for i in range(e):
        v1, v2, w = map(int, input().split())
        graph[v1][v2] = w

    print(floyd_warshall(v, graph))

if __name__ == "__main__":
    main()