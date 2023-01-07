# 문자열 압축
# 구현

def solution(s):
    answer = len(s)
    if len(s) == 1: # 문자열 길이가 1인 경우
        return 1
    
    half = len(s) // 2
    
    for i in range(1, half+1, 1):
        res = ''
        count = 1
        prev = s[0: i]
        
        for j in range(i, len(s), i):
            if prev == s[j: j+i]:
                count += 1
            else:
                if count >= 2:
                    res += (str(count) + prev)
                else:
                    res += prev
                prev = s[j: j+i]
                count = 1
        if count >= 2:
            res += (str(count) + prev)
        else:
            res += prev
        answer = min(answer, len(res))
    
    return answer