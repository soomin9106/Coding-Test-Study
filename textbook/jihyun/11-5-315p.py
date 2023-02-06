# 볼링공 고르기

"""
5 3
1 3 2 3 2
--> 8

8 5
1 5 4 3 2 4 5 2
--> 25
"""
from itertools import combinations

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    comb = list(combinations(arr, 2))
    
    for c in comb:
        if c[0] == c[1]:
            comb.remove(c)

    # print(comb, len(comb))
    print(len(comb))

main()