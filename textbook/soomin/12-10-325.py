# 자물쇠와 열쇠
# implementation

def rotate(mat):
    n = len(mat)
    m = len(mat[0])
    
    res = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = mat[i][j]
    return res

def check(lock):
    n = len(lock) // 3
    for i in range(n):
        for j in range(n):
            if lock[i+n][j+n] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    wide_lock = [[0] * (n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            wide_lock[i+n][j+n] = lock[i][j]
    
    for r in range(4):
        key = rotate(key)
        
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        wide_lock[x+i][y+j] += key[i][j] 
                if check(wide_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        wide_lock[x+i][y+j] -= key[i][j]
    return False