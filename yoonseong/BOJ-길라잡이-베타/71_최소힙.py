import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0: 
        if len(heap): # 0일 때 heap내에 원소가 있으면 heappop한 값을 print
            print(heapq.heappop(heap))
        else:
            print(0)
    else: # 0이 아니면, heappush로 입력한 값 heap에 삽입
        heapq.heappush(heap, num)
        
