# 기둥과 보 설치
# https://www.programmers.co.kr/learn/courses/30/lessons/60061

def valid_check(answer):
    for x, y, a in answer:
        # 기둥 설치일 때
        if not a:
            # 바닥이거나 보나 다른 기둥 위일 때
            if y == 0 or [x, y, 1] in answer or [x - 1, y , 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보 설치일 때
        else:
            # 한쪽 중 하나가 기둥이거나 두쪽 다 보일 때
            if [x, y, 0] in answer or [x + 1, y, 0] in answer or ([x, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    
    for bf in build_frame:
        x, y, a, b = bf
        
        # 설치일 때
        if b:
            answer.append([x, y, a])
            if not valid_check(answer):
                answer.remove([x, y, a])
                
        # 삭제일 때
        else:
            answer.remove([x, y, a])
            if not valid_check(answer):
                answer.append([x, y, a])
                
    answer.sort()
    return answer