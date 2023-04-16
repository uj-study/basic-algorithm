import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q=deque([(0,0)])
    melt=deque([])
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    while q:
        x,y=q.popleft()
        for dx,dy in dir:
            rx = x+dx
            ry = y+dy
            if 0<=rx<n and 0<=ry<m and not visited[rx][ry]:
                visited[rx][ry]=1
                if cheeze[rx][ry] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
                    q.append((rx, ry))
                elif cheeze[rx][ry] == 1:  # 치즈면 한 번에 녹이기 위해 melt에 넣음
                    melt.append((rx, ry))
    for x, y in melt:
        cheeze[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴

n,m=map(int,input().split())
cheeze=[]
cnt=0
for i in range(n):
    cheeze.append(list(map(int,input().split())))
    cnt += sum(cheeze[i])
time=1

while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:  # 치즈를 다 녹였으면
        print(time, meltCnt, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1

