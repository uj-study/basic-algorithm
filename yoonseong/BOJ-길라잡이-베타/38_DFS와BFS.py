import sys

def dfs(current):
    ans_dfs.append(current) # 방문 노드 추가
    visited[current] = 1    # 방문 표시

    for next in adj[current]:
        if not visited[next]: # 방문하지 않은 노드인 경우
            dfs(next)

def bfs(start):
    q = [] # 필요한 변수들 생성

    q.append(start) # 큐에 초기데이터(들) 삽입
    ans_bfs.append(start)
    visited[start] = 1

    while q:
        current = q.pop(0)
        for next in adj[current]:
            if not visited[next]: # 방문하지 않은 노드인 경우, 큐 삽입
                q.append(next)
                ans_bfs.append(next)
                visited[next] = 1

N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# adj 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(V)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)