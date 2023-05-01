import sys
import heapq

N = int(sys.stdin.readline())

leftHeap = [] # 중간값이 담길 최대힙
rightHeap = [] # 중간값보다 큰 값이 담길 최소힙

for i in range(N):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap): # leftHeap과 rightHeap의 길이가 같으면 left힙에 push
        heapq.heappush(leftHeap, (-num, num)) # left힙은 중간값이 들어간 힙으로 루트에 최대값(=중간값)이 들어가야함(파이썬은 기본적으로 최소힙 제공.)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and leftHeap[0][1] > rightHeap[0]: # leftHeap의 루트가 rightHeap의 루트보다 크면 두 값 체인지(짝수인 경우, 작은 값을 print해야함)
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)
        
        heapq.heappush(leftHeap, (-right, right))
        heapq.heappush(rightHeap, left[1])
    print(leftHeap[0][1])

# 시간초과
# heap = []
# for i in range(N):
#     num = int(sys.stdin.readline())
#     heapq.heappush(heap, num) # 우선, 입력값을 heap에 삽입
    
#     answer = 0
#     tmp = []

#     if len(heap) % 2: # heap의 길이가 홀수이면
#         for i in range(len(heap)//2 + 1): # heap길이의 절반+1 번째 원소가 중간값 (길이가 5인 경우 3번째가 중간값)
#             answer = heapq.heappop(heap) # answer을 heap길이의 절반+1만큼 갱신
#             tmp.append(answer) # heap에 다시 넣어주기 위해 tmp배열에 pop된 값 저장
#     else: # heap의 길이가 짝수이면
#         for i in range(len(heap)//2): # heap길이의 절반 인덱스 원소가 중간값 (길이가 4인 경우 2번째가 중간값)
#             answer = heapq.heappop(heap) # answer을 heap길이의 절반만큼 갱신
#             tmp.append(answer) # heap에 다시 넣어주기 위해 tmp배열에 pop된 값 저장
    
#     print(answer)
#     for t in tmp:
#         heapq.heappush(heap, t) # pop한 원소들을 다시 heap에 삽입
