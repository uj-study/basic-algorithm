import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num)) # 절댓값을 기준으로 최소힙
