# 팀 결성
# 서로소 집합 자료구조, 경로 압축
import sys

sys.stdin = open("textbook/soomin/practice/input.txt","rt")

n, m = map(int, input().split())

team = [0] * (n + 1)

for i in range(0, n+1):
    team[i] = i

def find_team(team, a):
    if team[a] != a:
        team[a] = find_team(team, team[a])
    return team[a]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)

    if b > a:
        team[b] = a
    else:
        team[a] = b

for i in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union_team(team, a, b)
    else:
        if find_team(team, a) == find_team(team, b):
            print('YES')
        else:
            print('NO')