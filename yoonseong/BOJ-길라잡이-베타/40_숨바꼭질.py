import sys
from collections import deque

MAX = 100001
N, K = map(int, sys.stdin.readline().split())

def bfs(start, end):
    # 1. q, visited 생성
    q = deque()
    visited = [0] * MAX 

    # 2. q.q(start) visited[start] = 1 ( 큐에 초기데이터 삽입, visited 초기화)
    q.append(start)
    visited[start] = 1

    # whilte q ~
    # current = q.pop(0)
    while q:
        current = q.popleft()
        if current == end:
            return visited[end] - 1
        # current-1, current+1, current*2가 방문 x일 경우 q삽입, visited에 표시
        for next in (current-1, current+1, current*2):
            if 0 <= next < MAX and visited[next] == 0: # MAX는 100001인데 인덱스는 0부터 시작하니 100000까지만 접근 가능. 따라서 MAX앞에 <
                # print('next & current & visited',next, current, visited[current])
                q.append(next)
                visited[next] = visited[current] + 1 # 깊이를 삽입
            
    return -1


answer = bfs(N, K)
print(answer)
    
