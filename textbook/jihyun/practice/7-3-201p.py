# 떡볶이 떡 만들기
"""
4 6
19 15 10 17

5 20
4 42 40 26 46
"""

def binary_search(arr, target, st, end):
    result = None

    while st <= end:
        remain = 0
        mid = (st + end) // 2

        for a in arr:
            if a > mid:
                remain += a - mid

        if remain >= target:
            result = mid
            st = mid + 1
        else:
            end = mid - 1
    return result

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    print(binary_search(arr, m, 0, max(arr) - 1))

if __name__ == "__main__":
    main()