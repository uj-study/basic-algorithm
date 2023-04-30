import sys
import heapq

N = int(sys.stdin.readline())

heap = []

# 기본적으로 최소힙을 제공
for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap):
            print(-heapq.heappop(heap)) # 뺄 때, 음수였던 값에 -1 을 곱해 양수로 만들어줌
        else:
            print(0)
    else:
        heapq.heappush(heap, -num) # 넣을 때, 음수로 만들어서 넣음 ( 큰 값이 음수가 됐을 때, 가장 작으므로 가장 상단에 위치 - 최소힙)
