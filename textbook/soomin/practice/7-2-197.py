# 부품 찾기
# 이진 탐색

import sys 

sys.stdin = open("binary_search/input.txt","rt")

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

m = int(input())
customers = list(map(int, input().split()))

for customer in customers:
    res = binary_search(num_list, customer, 0, n-1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
