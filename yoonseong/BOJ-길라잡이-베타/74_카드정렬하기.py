import sys
import heapq

N = int(sys.stdin.readline())

cards = []

for i in range(N):
  heapq.heappush(cards, int(sys.stdin.readline()))

answer = 0 

while len(cards) > 1:
  # 현재 남은 값 중, 가장 작은 두개의 값을 뽑아서 answer에 더해줌
  tmp1 = heapq.heappop(cards)
  tmp2 = heapq.heappop(cards)
  answer += tmp1 + tmp2
  heapq.heappush(cards, tmp1 + tmp2) # 해당 값을 다시 heap에 넣어서 추후에 또 더해줌

print(answer)

