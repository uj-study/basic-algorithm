import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

visited = [False for _ in range(n)] # true/false 로 팀 구분

min_diff = int(1e9) # min_diff의 초기값 무한대로 설정

def dfs(depth, idx):
    global min_diff

    if depth == n//2:
        start, link = 0, 0   # 팀 start (true), link (false)
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: # 탐색을 했으면 A팀
                    start += arr[i][j]
                elif not visited[i] and not visited[j]: # 탐색을 안했으면 B팀
                    link += arr[i][j]
        min_diff = min(min_diff, abs(start-link))

    for k in range(idx, n):
        if not visited[k]:
            visited[k] = True
            dfs(depth+1, k+1)
            visited[k] = False

dfs(0,0)
print(min_diff)

