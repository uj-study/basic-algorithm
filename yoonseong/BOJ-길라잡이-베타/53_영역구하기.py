import sys
from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    arr[x][y] = 1
    width = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in next_position:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0: # 범위 내 직사각형 아닌 영역
                q.append((nx, ny))
                arr[nx][ny] = 1
                width += 1
    return width

M, N, K = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(N)] for _ in range(M)]

next_position = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answers = []

# 이 부분 만들기가 중요.
for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 핵심
    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

# 좌표의 값이 0인 부분을 시작점으로 bfs실행
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
          answer = bfs(i, j)
          answers.append(answer)

print(len(answers))
answers.sort()
for a in answers:
    print(a, end=' ')
