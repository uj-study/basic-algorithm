import sys

N = int(sys.stdin.readline())
adj = []
visited = [[0] * N for j in range(N)]

answer = []

for i in range(N):
  data = list(map(int,sys.stdin.readline().rstrip()))
  adj.append(data)

# 시작위치를 받아서 해당 위치에 연결된 1의 개수(크기) 리턴
def bfs(startX, startY):
  # q 및 필요한 변수 생성
  q = []

  q.append((startX, startY)) # q 초기 데이터 삽입, 방문 표시, 크기를 위한 작업
  visited[startX][startY] = 1
  size = 1

  while q:
    currentX, currentY = q.pop(0) # 현재 x, y pop

    for dX, dY in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하좌우
      nextX, nextY = currentX + dX, currentY + dY
      # 범위 내 미방문 & 집이면 q 삽입
      if 0 <= nextX < N and 0 <= nextY < N and visited[nextX][nextY] == 0 and adj[nextX][nextY] == 1:
        q.append((nextX, nextY))
        visited[nextX][nextY] = 1
        size += 1
  return size

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0 and adj[i][j] == 1: # 방문하지 않았고, 집(1)이라면 bfs 수행
      answer.append(bfs(i, j))

answer.sort() # 크기 순 정렬
print(len(answer), *answer, sep='\n')