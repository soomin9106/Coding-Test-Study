# 상하좌우
# 시뮬레이션
import sys

sys.stdin = open("imple/input.txt","rt")

n = int(input())
move_list = list(map(str, input().split()))
node = (0,0)
for i in range(len(move_list)):
    if move_list[i] == 'R':
        nx = node[0]
        ny = node[1] + 1
        if ny > n-1:
            continue
        else:
            node = (nx, ny)
    elif move_list[i] == 'L':
        nx = node[0]
        ny = node[1] - 1
        if ny < 0:
            continue
        else:
            node = (nx, ny)
    elif move_list[i] == 'D':
        nx = node[0] + 1
        ny = node[1]
        if nx > n-1:
            continue
        else:
            node = (nx, ny)
    else:
        nx = node[0] - 1
        ny = node[1]
        if nx < 0:
            continue
        else:
            node = (nx, ny)
    # print(node)

print(node[0] + 1, end=' ')
print(node[1] + 1, end=' ')
