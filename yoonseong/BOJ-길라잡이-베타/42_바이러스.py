import sys

N = int(sys.stdin.readline()) # 컴퓨터 수
M = int(sys.stdin.readline()) # 연결된 간선 수
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

answer = 0

for i in range(1, M+1):
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

def dfs(current):
    global answer
    visited[current] = 1
    answer += 1

    for next in adj[current]:
        if visited[next] == 0:
            dfs(next)
dfs(1)
print(answer - 1) # 처음 제외
