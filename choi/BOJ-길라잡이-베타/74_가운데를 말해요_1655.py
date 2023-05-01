import sys, heapq
input = sys.stdin.readline

n = int(input())
left = []
right = []

# 중간보다 작 왼 큰 오
for i in range(n):
    num = int(input().rstrip())
    # 반씩 나눠서 넣기
    if len(left) == len(right):
        heapq.heappush(left,(-num, num))    # 최대힙
    else :
        heapq.heappush(right,(num, num))
    
    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))

    print(left[0][1])