import sys

N = int(sys.stdin.readline())
ability = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
res = INF

# DFS
def DFS(L,idx):
    global res
    if L == N//2:
      # print("내부", L, idx, visited)
      A = 0
      B = 0
      for i in range(N):
        for j in range(N):
          if visited[i] and visited[j]:
            A += ability[i][j]
          elif not visited[i] and not visited[j]:
            B += ability[i][j]
      res = min(res, abs(A-B))
      return
    for i in range(idx,N):
      if not visited[i]:
        visited[i] = True
        # print("전", L, idx, i, visited)
        DFS(L+1,i+1)
        visited[i] = False
        # print("후", L, idx, i, visited)

# print(ability)            
DFS(0,0)
print(res)

