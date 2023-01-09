# 위에서 아래로
"""
3
15
27
12
"""

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(sorted(arr, key=lambda x:-x))