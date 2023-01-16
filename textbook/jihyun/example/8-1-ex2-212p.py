# 피보나치 수열 메모이제이션
from time import time

MAX_LEN = 99

def fibonacci(x):
    if x == 1 or x == 2:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)

def fibo_memoization(d, x):

    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]

    d[x] = fibo_memoization(d, x - 1) + fibo_memoization(d, x - 2)
    
    return d[x]

def fibo_bottom_up(d, x):
    d[1], d[2] = 1, 1

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]
    
    return d[x]

def main():
    st = time()
    print(fibonacci(30))
    print(f"time: {time() - st}")

    d = [0] * (MAX_LEN + 1)
    st = time()
    print(fibo_memoization(d, 30))
    print(f"time: {time() - st}")

    d = [0] * (MAX_LEN + 1)
    st = time()
    print(fibo_bottom_up(d, 30))
    print(f"time: {time() - st}")

if __name__ == "__main__":
    main()