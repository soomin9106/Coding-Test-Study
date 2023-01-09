# 실패율
"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""

def solution(N, stages):
    answer = []
    count = [0] * (N + 1)
    
    for s in stages:
        count[s - 1] += 1
    
    length = len(stages)
    fail_rates = []
    
    for i in range(N):
        if count[i] == 0:
            fail_rate = 0
        else:
            fail_rate = count[i] / length
            length -= count[i]   
        
        fail_rates.append((i + 1, fail_rate))
    
    fail_rates.sort(key=lambda x: -x[1])
    for f in fail_rates:
        answer.append(f[0])
    
    return answer