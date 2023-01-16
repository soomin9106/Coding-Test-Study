# 1로 만들기

MAX_LEN = 30000

def solution(d, x):
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[x]

def main():
    x = int(input())
    # d = [0] * (MAX_LEN + 1)
    d = [0] * (x + 1)

    print(solution(d, x))
    print(d[1:x + 1])

if __name__ == "__main__":
    main()