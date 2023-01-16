# 효율적인 화폐 구성
"""
2 15
2
3

3 4
3
5
7
"""

def solution(d, units, target):
    for unit in units:
        d[unit] = 1
        for i in range(unit, target + 1, unit):
            d[i] = min(d[i - unit] + 1, d[i])

    if d[target] != 10001:
        return d[target]
    else:
        return -1

def main():
    n, target = map(int, input().split())

    d = [10001] * 101

    units = []
    for i in range(n):
        units.append(int(input()))

    print(solution(d, units, target))

if __name__ == "__main__":
    main()