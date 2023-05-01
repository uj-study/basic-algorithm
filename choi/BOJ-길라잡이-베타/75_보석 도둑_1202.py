import sys, heapq
input = sys.stdin.readline

n, k = map(int,input().split())
mv = []
c = []
for i in range(n):
    heapq.heappush(mv,list(map(int,input().split())))
for i in range(k):
    c.append(int(input().rstrip()))
c.sort()

ans = 0
tmp_price = []
# 가방 최대무게 적은거부터
for i in c:
    while mv and i >= mv[0][0]:
        heapq.heappush(tmp_price, -heapq.heappop(mv)[1])    # 최대힙

    if tmp_price:
        ans -= heapq.heappop(tmp_price) 
    elif not mv:
        break
print(ans)