# 카드 정렬하기
# heapq 사용
# https://www.acmicpc.net/problem/1715

import sys
sys.stdin = open("textbook/soomin/input.txt","rt")

import heapq

n = int(input())

num_list = []
for _ in range(n):
    heapq.heappush(num_list, int(input()))


if len(num_list) == 1:
    print(0)
    exit(0)

res = 0

while len(num_list) > 1:
    hap = heapq.heappop(num_list) + heapq.heappop(num_list)
    res += hap
    heapq.heappush(num_list, hap)

print(res)