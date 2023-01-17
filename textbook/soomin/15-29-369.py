# 공유기 설치
# binary search
# https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())

wifi_list = []

for _ in range(n):
    wifi_list.append(int(input()))

wifi_list = sorted(wifi_list)

start = 1
end = wifi_list[-1] - wifi_list[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    pt = wifi_list[0]
    for i in range(1, len(wifi_list)):
        if wifi_list[i] >= pt + mid:
            pt = wifi_list[i]
            count += 1

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)