# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    heap = []

    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i))

    prev = 0
    while k > len(heap):
        root = heapq.heappop(heap)[1]

        height = root - prev
        width = len(heap)

        k -= height * width

        prev = root
    
    print(k)


def main():
    food_times = [3, 5, 1, 6, 5, 3]
    k = 20

    solution(food_times, k)

main()