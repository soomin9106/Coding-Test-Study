# 바닥 공사

def solution(d, n):
    d[1] = 1
    d[2] = 3

    for i in range(3, n + 1):
        d[i] = d[i - 1] + 2 * d[i - 2] % 796796

    return d[n]

def main():
    n = int(input())
    d = [0] * (n + 1)

    print(solution(d, n))

if __name__ == "__main__":
    main() 