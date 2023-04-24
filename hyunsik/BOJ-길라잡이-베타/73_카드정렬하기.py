import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

cards = []

for _ in range(n):
    heappush(cards, int(input()))

ans = 0

while len(cards) > 1:
    card1 = heappop(cards)
    card2 = heappop(cards)
    ans += card1 + card2
    heappush(cards, card1 + card2)

print(ans)