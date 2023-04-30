import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    b = int(input())
    if b == 0:
        if a:
            print(heapq.heappop(a)[1])
        else:
            print(0)
    else:
        heapq.heappush(a, (abs(b), b))