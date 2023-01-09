# 성적이 낮은 순서로 학생 출력하기
"""
4
홍길동 95
이순신 77
박정후 64
이경은 98
"""

n = int(input())

arr = []
for i in range(n):
    name, score = input().split()
    score = int(score)

    arr.append((name, score))

arr = sorted(arr, key=lambda x: x[1])

for a in arr:
    print(a[0], end=' ')
print()
