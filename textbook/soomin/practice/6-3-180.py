# 성적이 낮은 순서로 학생 출력하기
import sys

sys.stdin = open("sort/input.txt","rt", encoding='UTF8')


n = int(input())

arr = []

for i in range(n):
    name, score = map(str, input().split())
    arr.append((name, int(score)))

arr = sorted(arr, key = lambda x: x[1])

for element in arr:
    print(element[0], end=' ')