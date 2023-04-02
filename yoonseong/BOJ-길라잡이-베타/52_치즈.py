import sys
from collections import deque

def bfs():
    q = deque([])
    visited = [[0 for _ in range(col)] for _ in range(row)]

    q.append((0, 0))
    visited[0][0] =1
    left = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in next_position:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0:
                if cheeze[nx][ny] == 0: # 가장자리인 경우에만 q에 넣어줌
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif cheeze[nx][ny] == 1: # 치즈, 녹여야함
                  cheeze[nx][ny] = 0
                  visited[nx][ny] = 1
                  left += 1
    return left

row, col = map(int, sys.stdin.readline().split()) # 세로, 가로

cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

next_position = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0 
left_cheeze = [] # 남은 치즈 수

while True:
    count = bfs()
    left_cheeze.append(count)

    if count == 0:
        break
    
    time += 1

print(time)
print(left_cheeze[-2]) # 다 녹기 한 시간 전 개수.
