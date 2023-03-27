import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split()) # 가로, 세로
tomato = []
q = deque([])

next_position = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

for i in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M): # 가로 길이
        if tomato[i][j] == 1:
            q.append([i, j])

def BFS():
    while q:
        cX, cY = q.popleft()
        for dX, dY in next_position:
            nX, nY = dX + cX, dY + cY
            if 0 <= nX < N and 0 <= nY < M and tomato[nX][nY] == 0: # nX가 세로이기 때문에 N보다 작은 범위, nY가 가로이기 때문에 M보다 작은 범위
                q.append([nX, nY])
                tomato[nX][nY] = tomato[cX][cY] + 1

BFS()
answer = 0

for t in tomato:
    for j in t:
        if j == 0:
            print(-1)
            exit()
    answer = max(max(t), answer)

print(answer-1) # 첫날을 1로 시작. 따라서 -1