# 부품 찾기
MAXLEN = 1000000

"""
5
8 3 7 9 2
3
5 7 9
"""

def binary_search(arr, target, st, end):
    while st <= end:
        mid = (st + end) // 2

        if arr[mid] == target:
            return "yes"
        elif arr[mid] > target:
            end = mid - 1
        else:
            st = mid + 1
    
    return "no"

def count_sort(arr, targets):
    count = [0] * (MAXLEN + 1)

    for a in arr:
        count[a] += 1
    
    for target in targets:
        if count[target] == 0:
            print("no", end=" ")
        else:
            print("yes", end=" ")

    print()

def use_set(arr, targets):
    arr = set(arr)

    for target in targets:
        if target in arr:
            print("yes", end=" ")
        else:
            print("no", end=" ")
    
    print()

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        result = binary_search(arr, target, 0, n - 1)
        print(result, end=" ")

    print()

    count_sort(arr, targets)
    use_set(arr, targets)

if __name__ == "__main__":
    main()