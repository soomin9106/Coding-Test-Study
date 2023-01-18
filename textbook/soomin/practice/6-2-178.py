# 위에서 아래로

import sys 

sys.stdin = open("sort/input.txt","rt")

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

print(arr)