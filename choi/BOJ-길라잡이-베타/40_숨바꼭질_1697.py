import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == y:
            return arr[x]
        for i in (x-1, x+1, 2*x):
            if 0 <= i < 100001 and not arr[i]:
                arr[i] = arr[x] + 1
                q.append(i)

            
x, y = map(int,input().split())
arr = [0]*100001
print(bfs(x))