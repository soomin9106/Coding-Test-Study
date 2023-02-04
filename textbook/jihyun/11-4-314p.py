# 만들 수 없는 금액
"""
5
3 2 1 1 9

3
3 5 7

3
1 1 1

3
1 1 2
"""

def my_solution(units):
    target = 1

    if target < units[0]:
        return target

    total = sum(units)

    # while True:
    for target in range(2, total):
        possible = []

        for u in units:
            if u < target:
                possible.append(u)

        possible.sort(key=lambda x: -x)

        temp = target
        for p in possible:
            if temp >= p:
                temp -= p

            if temp == 0:
                break

        if temp != 0:
            return target

    return total + 1

def solution(units):
    target = 1

    for u in units:
        if target < u:
            break
        
        target += u
    
    return(target)

def main():
    n = int(input())
    units = list(map(int, input().split()))
    units.sort()

    print("mine:", my_solution(units))
    print("sol:", solution(units))

main()
