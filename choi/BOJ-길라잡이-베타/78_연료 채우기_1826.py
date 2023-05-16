import sys, heapq
input = sys.stdin.readline

n = int(input())
gas = []
for i in range(n):
    gas.append(list(map(int, input().split())))
gas.sort(key=lambda x: x[0])
l, p = map(int,input().split())

now_loc = 0
now_gas = p
ans = 0
heap = []

for i in range(n):
    distance = gas[i][0] - now_loc

    while now_gas < distance:
        if not heap:
            print(-1)
            exit()
        
        now_gas += -heapq.heappop(heap)
        ans += 1

    now_gas -= distance
    now_loc = gas[i][0]        

    heapq.heappush(heap,-gas[i][1])

# 마지막 도착지점에서는 주유를 하지 않아도 됨
while now_gas < l - now_loc:
    if not heap:
        print(-1)
        exit()
        
    now_gas += -heapq.heappop(heap)
    ans += 1
    
print(ans)
        