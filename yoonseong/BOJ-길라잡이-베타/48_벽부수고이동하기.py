import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # N 세로, M 가로
wall = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
next_position = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    wall.append(list(map(int, sys.stdin.readline().rstrip())))

def BFS(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1

    while q:
        cX, cY, cZ = q.popleft()
        if cX == N-1 and cY == M-1:
            return visited[cX][cY][cZ]
        for dX, dY in next_position:
            nX, nY = cX + dX, cY + dY
            if 0  <= nX < N and 0 <= nY < M:
                if wall[nX][nY] == 0 and visited[nX][nY][cZ] == 0: # 현재 위치로 이동할 수 있고, 아직 방문하지 않았다면
                  q.append((nX, nY, cZ))
                  visited[nX][nY][cZ] = visited[cX][cY][cZ] + 1
                elif wall[nX][nY] == 1 and cZ == 0: # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                    q.append((nX, nY, cZ + 1))
                    visited[nX][nY][cZ + 1] = visited[cX][cY][cZ] + 1
    return -1 # 목표지점까지 도달하지 못한다면 -1 리턴
                    

print(BFS(0, 0, 0))
