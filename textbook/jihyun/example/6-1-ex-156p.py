import random
from time import time
# 정렬 알고리즘 공부

def seleciton_sort(arr):
    st = time()

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # print(f'min_idx: {min_idx}')
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"\nselection sort: {time() - st}s\n{arr}")

def insertion_sort(arr):
    st = time()

    for i in range(1, len(arr)):
        for j in range(i, 0 ,-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
    print(f"\ninsertion sort: {time() - st}s\n{arr}")

def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

def count_sort(arr):
    st = time()

    count = [0] * (max(arr) + 1)
    result = []

    for a in arr:
        count[a] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)

    print(f"\ncount sort: {time() - st}s\n{result}")


def main(n):
    arr = [random.randint(1, n) for i in range(n)]

    print("first arr:", arr)

    seleciton_sort(arr)
    insertion_sort(arr)

    st = time()
    quick_sort(arr, 0, len(arr) - 1)
    print(f"\nquick sort: {time() - st}s\n{arr}")

    count_sort(arr)

main(20)