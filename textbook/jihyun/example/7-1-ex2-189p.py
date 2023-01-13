# 이진 검색 구현

"""
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 5 6 9 11 13 15 17 19
"""

def binary_search_recursion(arr, target, st, end):
    if st > end:
        return None
    
    mid = (st + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursion(arr, target, st, mid - 1)
    else:
        return binary_search_recursion(arr, target, mid + 1, end)

def binary_search_loop(arr, target, st, end):
    while st <= end:
        mid = (st + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            st = mid + 1

    return None

def main():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    recur_find = binary_search_recursion(arr, target, 0, n - 1)
    loop_find = binary_search_loop(arr, target, 0, n - 1)

    if recur_find:
        print(f"{target} is found at arr[{recur_find}]!")
    else:
        print("Not found")

    if loop_find:
        print(f"{target} is found at arr[{loop_find}]!")
    else:
        print("Not found")

if __name__ == "__main__":
    main()