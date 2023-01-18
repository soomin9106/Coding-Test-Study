# 왕실의 나이트

import sys

sys.stdin = open("imple/input.txt","rt")

node = input()
col = ord(node[0]) - 96
row = int(node[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

res = 0

for step in steps:
    nr = row + step[0]
    nc = col + step[1]

    if nr >= 1 and nr <=8 and nc >= 1 and nc <=8:
        res += 1

print(res)
