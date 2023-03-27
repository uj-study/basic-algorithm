import sys
input = sys.stdin.readline
from collections import deque

dir = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(graph, x, y, l):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0 
    cnt = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for dx, dy in dir:
            rx, ry = x+dx, y+dy
            if (rx < 0 or rx >=l or ry < 0 or ry >= l):
                continue
            if graph[rx][ry] == 1:
                graph[rx][ry] = 0
                q.append((rx, ry))
                cnt += 1
    return cnt



N = int(input())
graph = []
result = []

for i in range(N):
    graph.append(list(map(int,input().rstrip())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(graph, i, j, N)
            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)
