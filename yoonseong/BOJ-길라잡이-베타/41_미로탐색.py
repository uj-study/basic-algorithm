import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visited = [[0] * M for _ in range(N)]
adj = []

for i in range(N):
    adj.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(si, sj):
    q = deque()

    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        if ci == N-1 and cj == M-1: # 끝에 도착
            return visited[ci][cj]
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
          ni, nj = di + ci, dj + cj
          if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and adj[ni][nj] == 1:
            q.append((ni, nj))
            visited[ni][nj] = visited[ci][cj] + 1 # 이전 깊이에 하나 더 추가한 값 (이동거리)

print(bfs(0, 0))
