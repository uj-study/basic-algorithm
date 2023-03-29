import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
answer = 0

tomato = []
q = deque([])
next_position = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)] # 상하좌우, 위칸아래칸 

for i in range(H):
    layer = []
    for j in range(N):
        data = list(map(int, sys.stdin.readline().split()))
        layer.append(data)
        for k in range(M):
            if data[k] == 1:
                q.append([i, j, k])
    tomato.append(layer)

while q:
    height, row, col = q.popleft()
    for dh, dr, dc in next_position:
        nh, nr, nc = height + dh, row + dr, col + dc
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tomato[nh][nr][nc] == 0: # 범위 내에 있고 토마토가 익지 않은 상태(0)인 경우
            tomato[nh][nr][nc] = tomato[height][row][col] + 1
            q.append([nh, nr, nc])

for i in tomato:
    for j in i:
      if j.count(0):
          print(-1)
          exit()
      answer = max(answer, max(j))
print(answer-1)        