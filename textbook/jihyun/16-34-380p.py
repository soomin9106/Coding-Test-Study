# 병사 배치하기

"""
7
15 11 4 8 5 2 4
"""

def solution(d, arr):
    n = len(arr)

    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:
                d[i] = max(d[i], d[j] + 1)
            # print(f"d[{i}]: {d[i]}")
    print(d)
    return n - max(d)



def main():
    n = int(input())
    # d = [x + 1 for x in range(n)]
    d = [1] * n

    arr = list(map(int, input().split()))

    print(solution(d, arr))

if __name__ == "__main__":
    main()