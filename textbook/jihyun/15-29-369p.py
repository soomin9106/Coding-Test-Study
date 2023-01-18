# 공유기 설치
# https://www.acmicpc.net/problem/2110

"""
5 3
1
2
8
4
9
--> 3
"""

# 공유기를 설치할 거리를 이분 탐색으로 결정

def solution(arr, c, st, end):
    if c == 2:
        return end

    while st <= end:
        mid = (st + end) // 2
        cur = arr[0]
        ct = 1

        for i in range(len(arr)):
            if arr[i] - cur >= mid:
                ct += 1
                cur = arr[i]

        if ct < c:
            end = mid - 1
        else:
            st = mid + 1
            result = mid
    
    return result

def main():
    n, c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    
    arr.sort()

    # st = min dist, end = max dist
    print(solution(arr, c, 1, arr[-1] - arr[0]))

if __name__ == "__main__":
    main()