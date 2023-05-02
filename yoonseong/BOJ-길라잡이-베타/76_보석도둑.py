import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewelryInfo = [] # 보석정보
bags = [] # 가방 정보

for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewelryInfo.append((M, V))

for i in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)

jewelryInfo.sort() # 무게가 가벼운 보석이 앞에 오도록 정렬
bags.sort() # 적은 무게를 담을 수 있는 가방이 앞에 위치하도록 정렬

answer = 0
tmp = []

for bag in bags:
    while jewelryInfo and jewelryInfo[0][0] <= bag: # 보석 정보가 있고, 보석의 무게가 가방의 무게 이하일 때 까지 pop
        heapq.heappush(tmp, -jewelryInfo[0][1]) # 보석 가격이 높은게 루트에 위치하도록 -를 곱해서 heap에 push (최대힙)
        heapq.heappop(jewelryInfo)

    # 처음에는
    # 다음 가방을 위해, answer에 더해줄 tmp값을 제외하고는 다시 jewerlyInfo에 넣어주어야하는게 아닌가 생각했지만
    # 이미 tmp에 최대힙으로 값들이 들어가있어서 그럴 필요가 없다는걸 느낌.
    if tmp:
        answer += -heapq.heappop(tmp)

print(answer)
