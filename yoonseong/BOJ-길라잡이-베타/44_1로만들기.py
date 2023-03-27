import sys
from collections import deque

N = int(sys.stdin.readline())
visited = [0] * (N+1)

def BFS(num):
    q = deque()
    q.append(num)

    while q:
        cur = q.popleft()

        if cur == 1:
            return visited[cur]
        
        if cur % 3 == 0 and visited[cur//3] == 0:
            q.append(cur//3)
            visited[cur//3] = visited[cur] + 1
        if cur % 2 == 0 and visited[cur//2] == 0:
            q.append(cur//2)
            visited[cur//2] = visited[cur] + 1
        if visited[cur-1] == 0:
            q.append(cur-1)
            visited[cur-1] = visited[cur] + 1
    
BFS(N)
print(visited[1])