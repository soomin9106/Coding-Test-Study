# 미래 도시

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
--> 3

4 2
1 3
2 4
3 4
--> -1
"""
import sys

INF = int(1e9)
input = sys.stdin.readline

def solution(n, graph, x, k):
    for p in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])

    result = graph[1][k] + graph[k][x]

    if result >= INF:
        return "-1"

    return result

def main():
    n, m = map(int, input().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    x, k = map(int, input().split())

    print(solution(n, graph, x, k))

if __name__ == "__main__":
    main()
