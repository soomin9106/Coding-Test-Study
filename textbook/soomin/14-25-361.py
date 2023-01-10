# 실패율

from collections import defaultdict

def solution(N, stages):
    answer = []
    fail_dict = defaultdict(int)
    total = len(stages)
    
    for i in range(1, N+1, 1):
        if total == 0:
            fail_dict[i] = 0
            continue
        count = 0
        for j in range(len(stages)):
            if stages[j] == i:
                count += 1
        if total != 0:
            fail_dict[i] = count / total
            total -= count
        else:
            fail_dict[i] = 0
            break
            
    fail_dict = sorted(fail_dict.items(), key = lambda x: x[1], reverse = True)
    
    for element in fail_dict:
        answer.append(element[0])
    return answer