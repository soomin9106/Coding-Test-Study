# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059#

def rotate(mat):
    n = len(mat)
    m = len(mat[0])
    
    res = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = mat[i][j]
            
    return res

def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
                    
            
    new_len = n + 2 * (m - 1)
    new_lock = [[0 for _ in range(new_len)] for _ in range(new_len)]
    
    for i in range(m - 1, m + n - 1):
        for j in range(m - 1, m + n - 1):
            new_lock[i][j] = lock[i - m + 1][j - m + 1]
    
    # 아래로 이동
    for i in range(new_len - m + 1):
        # 옆으로 이동
        for j in range(new_len - m + 1):
            # 네 가지 방향 체크
            for p in range(4):
                answer = True
                key = rotate(key)
                # key와 lock xor 연산
                for k in range(m):
                    for l in range(m):
                        # 자물쇠와 겹칠 때
                        if m - 1 <= i + k < m + n - 1 and m - 1 <= j + l < m + n - 1:
                            new_lock[i + k][j + l] = key[k][l] ^ new_lock[i + k][j + l]
                    
                # lock 확인
                for k in range(m - 1, m + n - 1):
                    for l in range(m - 1, m + n - 1):
                        if not new_lock[k][l]:
                            answer = False
                            break
                    
                if answer:
                    print(f"i: {i}  j: {j}")
                    return True
                else:
                    # 아니면 다시 되돌려놓기
                    for k in range(m - 1, m + n - 1):
                        for l in range(m - 1, m + n - 1):
                            new_lock[k][l] = lock[k - m + 1][l - m + 1]
        
    return False