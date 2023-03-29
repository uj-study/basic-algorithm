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



# 추가
# import sys
# from collections import deque

# def bfs():
#     # 1. q생성, visited[] 생성
#     q = deque([])
#     visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    
#     # 2. q에 초기데이터 삽입 & 안 익은 토마토(0) 카운트
#     cnt = 0
#     for h in range(H):
#         for i in range(N):
#             for j in range(M):
#                 if arr[h][i][j] == 1: # 익은 토마토
#                     q.append([h, i, j])
#                     visited[h][i][j] = 1
#                 elif arr[h][i][j] == 0: # 익지 않은 토마토
#                     cnt += 1

#     while q:
#         height, row, col = q.popleft()
#         # 범위 내, 악 인은 토마토
#         for dh, dr, dc in next_position:
#             nh, nr, nc = height + dh, row + dr, col + dc
#             if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and visited[nh][nr][nc] == 0 and arr[nh][nr][nc] == 0: # 범위 내에 있고 토마토가 익지 않은 상태(0)인 경우
#               visited[nh][nr][nc] = visited[height][row][col] + 1
#               q.append([nh, nr, nc])
#               cnt -= 1 # 안 익은 토마토 감소
    
#     if cnt == 0: # 모두 익음
#         return visited[height][row][col] - 1
#     else:
#         return -1

# M, N, H = map(int, sys.stdin.readline().split())
# arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
# next_position = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)] # 상하좌우, 위칸아래칸 
# answer = bfs()
# print(answer)