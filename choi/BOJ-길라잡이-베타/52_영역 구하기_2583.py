import sys
input = sys.stdin.readline
from collections import deque

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):  # 직사각형 표시
        for j in range(x1,x2):
            graph[i][j] = 1

result=[]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    cnt = 1
    while q:
        y,x = q.popleft()
        for dy,dx in dir:
            ry = y + dy
            rx = x + dx
            if 0<=rx<n and 0<=ry<m and graph[ry][rx] == 0:
                graph[ry][rx] = 1
                q.append((ry,rx))
                cnt += 1
    return cnt

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i,j))

print(len(result))
print(*sorted(result))