# 피보나치 수열 메모이제이션
from time import time

MAX_LEN = 99
d = [0] * (MAX_LEN + 1)

def fibonacci(x):
    if x == 1 or x == 2:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)

def fibo_memoization(x):

    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]

    d[x] = fibo_memoization(x - 1) + fibo_memoization(x - 2)
    
    return d[x]

def main():
    st = time()
    print(fibonacci(30))
    print(f"time: {time() - st}")

    st = time()
    print(fibo_memoization(30))
    print(f"time: {time() - st}")

if __name__ == "__main__":
    main()