import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int,input().split())
graph = []
q=deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append([i,j,k])
    graph.append(temp)

dir = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

while(q):
    x,y,z = q.popleft()

    for dx, dy, dz in dir:
        rx = x + dx
        ry = y + dy
        rz = z + dz
        if 0<=rx<h and 0<=ry<n and 0<=rz<m and graph[rx][ry][rz] == 0:
            q.append([rx,ry,rz])
            graph[rx][ry][rz] = graph[x][y][z] + 1

day=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)