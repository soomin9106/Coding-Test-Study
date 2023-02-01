# 볼링공 고르기

import sys
from collections import defaultdict
sys.stdin = open("textbook/soomin/input.txt","rt")

n, m = map(int, input().split())

ball_list = list(map(int, input().split()))

weight = [0] * 11

for i in ball_list:
    weight[i] += 1

temp = n
answer = 0

for w in weight:
    temp -= w
    answer += temp * w

print(answer)