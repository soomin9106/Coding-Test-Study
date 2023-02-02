# 연산자 끼워넣기
# backtracking
# https://www.acmicpc.net/problem/14888

import sys
sys.stdin = open("textbook/soomin/input.txt","rt")


n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

ops = []
for idx, op in enumerate(op_list):
    for i in range(op):
        if idx == 0:
            ops.append('+')
        elif idx == 1:
            ops.append('-')
        elif idx == 2:
            ops.append('*')
        else:
            ops.append('//')


def dfs(L, sum, op_combi):
    global mini
    global maxi

    if L == n:
        maxi = max(maxi, sum)
        mini = min(mini, sum)
        return
    else:
        if op_combi.count('+'):
            op_combi.remove('+')
            dfs(L + 1, sum + num_list[L], op_combi)
            op_combi.append('+')
        if op_combi.count('-'):
            op_combi.remove('-')
            dfs(L + 1, sum - num_list[L], op_combi)
            op_combi.append('-')
        if op_combi.count('*'):
            op_combi.remove('*')
            dfs(L + 1, sum * num_list[L], op_combi)
            op_combi.append('*')
        if op_combi.count('//'):
            op_combi.remove('//')
            dfs(L + 1, int(sum / num_list[L]), op_combi)
            op_combi.append('//')

    



maxi = -1e9
mini = 1e9

dfs(1, num_list[0], ops)

print(maxi)
print(mini)