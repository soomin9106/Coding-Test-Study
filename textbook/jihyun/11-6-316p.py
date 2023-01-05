# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []

    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i))

    prev = 0
    while True:
        length = len(heap)
        root = heap[0][0]

        height = root - prev
        width = length
        area = height * width

        if k < area:
            break

        k -= height * width

        prev = root
        heapq.heappop(heap)

    heap.sort(key=lambda x:x[1])
    print(heap)

    x = k % len(heap)
    print(heap[x][1] + 1)

    return heap[x][1] + 1
    


def main():
    food_times = [3, 5, 1, 6, 5, 3]
    k = 20

    solution(food_times, k)

main()