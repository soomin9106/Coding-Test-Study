# 떡볶이 떡 만들기
# 이진 탐색

import sys 

sys.stdin = open("binary_search/input.txt","rt")

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for element in array:
        if element > mid:
            total += (element - mid)

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)