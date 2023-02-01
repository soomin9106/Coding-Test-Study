# 기둥과 보 설치
# implementation

def isValid(n, answer):
    for x, y, t in answer:
        if t == 0: # 기둥
            if y == 0 or [x, y - 1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                    continue
            else:
                return False
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
                    

def solution(n, build_frame):
    answer = []
    
    for bf in build_frame:
        x, y, a, b = bf
        
        if b == 0: # remove case
            if [x, y, a] in answer:
                answer.remove([x, y, a])
            if not isValid(n, answer): # 지우면 안된다면 다시 넣기
                answer.append([x, y, a])
        else: # add case
            answer.append([x, y, a])
            if not isValid(n, answer): # 더했을 때 안된다면 다시 빼기 
                answer.remove([x, y, a])
    answer = sorted(answer, key = lambda x: (x[0], x[1], x[2]))    
    return answer