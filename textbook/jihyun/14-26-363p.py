# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

"""
3
10
20
40
"""
import heapq

def main():
    n = int(input())
    heap = []

    for _ in range(n):
        heapq.heappush(heap, int(input()))
    
    total = 0
    while len(heap) > 1:
        top = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, top + second)
        # print(arr[1])
        total += top + second
        # print(arr)

    print(total)

main()