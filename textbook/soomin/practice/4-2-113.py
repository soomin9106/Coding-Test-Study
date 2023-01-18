# 시각
# 00시 00분 00ch ~ N시 59분 59초까지 모든 시각 중 3이 하나라도 포함
# 완전 탐색

import sys

sys.stdin = open("imple/input.txt","rt")

n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)