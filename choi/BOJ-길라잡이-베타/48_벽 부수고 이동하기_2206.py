import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dir = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y,z):
    q= deque()
    q.append((x,y,z))

    while q:
        a,b,c = q.popleft()

        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for dx,dy in dir:
            rx = a + dx
            ry = b + dy
            if rx < 0 or rx >= n or ry < 0 or ry >= m:
                continue
            
            if graph[rx][ry] == 1 and c == 0:
                visited[rx][ry][1] = visited[a][b][0] + 1
                q.append((rx, ry, 1))

            elif graph[rx][ry] == 0 and visited[rx][ry][c] == 0:
                visited[rx][ry][c] = visited[a][b][c] + 1
                q.append((rx, ry, c))
    return -1

print(bfs(0,0,0))