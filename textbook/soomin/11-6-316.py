# 무지의 먹방 라이브
# 그리디 알고리즘
# 우선순위 힙큐 구조

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    val = 0
    prev = 0
    length = len(food_times)
    
    while val + ((q[0][0] - prev) * length) <=k:
        now = heapq.heappop(q)[0]
        val += (now - prev) * length
        length -= 1
        prev = now
        
    result = sorted(q, key = lambda x: x[1])
    return result[(k-val) % length][1]
        