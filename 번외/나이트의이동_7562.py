import sys
from collections import deque

T = int(sys.stdin.readline())
next_position = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]

def BFS(size, startX, startY, endX, endY):
    q = deque()
    visited = [[0] * size for _ in range(size)]

    q.append((startX, startY))
    visited[startX][startY] = 0

    while q:
        curX, curY = q.popleft()

        if curX == endX and curY == endY:
            return visited[curX][curY]

        for dX, dY in next_position: # 8방향 이동
            nX, nY = curX + dX, curY + dY
            if 0 <= nX < size and 0 <= nY < size and visited[nX][nY] == 0: # 다음 지점이 체스판 범위 내이고, 방문하지 않았다면
                q.append((nX, nY))
                visited[nX][nY] = visited[curX][curY] + 1

for i in range(T):
    size = int(sys.stdin.readline())
    current = list(map(int, sys.stdin.readline().split()))
    destination = list(map(int, sys.stdin.readline().split()))
    answer = BFS(size, current[0], current[1], destination[0], destination[1])
    print(answer)