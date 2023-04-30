import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    b = int(input())
    if b == 0:
        if a:
            print(-1*heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, -b)