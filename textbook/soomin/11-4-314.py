# 만들 수 없는 금액
# 그리디 알고리즘

import sys
sys.stdin = open("textbook/soomin/input.txt","rt")

n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

target = 1

for num in num_list:
    if target < num:
        break
    target += num

print(target)