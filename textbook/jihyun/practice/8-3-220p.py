# 개미 전사
"""
4
1 3 1 5
"""

def solution(d, k):
    d[0] = k[0]
    d[1] = max(k[0], k[1])
    for i in range(2, len(k)):
        d[i] = max(d[i - 1], d[i - 2] + k[i])

    print(d[len(k) - 1])

def main():
    n = int(input())
    d = [0] * n

    k = list(map(int, input().split()))

    solution(d, k)

if __name__ == "__main__":
    main()