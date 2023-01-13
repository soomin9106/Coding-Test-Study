# 병사 배치하기 
# dynamic programming, 가장 긴 증가하는 부분 수열
# 링크 : https://www.acmicpc.net/problem/18353

# import sys

# sys.stdin = open("textbook/soomin/input.txt","rt")

n = int(input())
array = list(map(int, input().split()))

d = [1] * n

for i in range(n):
    for j in range(i):
        if array[j] > array[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
