import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input().rstrip()))

heapq.heapify(cards)
cnt = 0

while len(cards) > 1:   # 정리할 카드있으면
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)  # 정리해서 추가
    cnt += tmp
    
print(cnt)
