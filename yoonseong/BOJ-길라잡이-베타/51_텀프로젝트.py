import sys
sys.setrecursionlimit(10 ** 7)

def dfs(x):
    global ans
    visited[x] = True
    cycle.append(x)
    num = arr[x]

    if visited[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):] # 순환될 때 마지막 원소가 가르키는 곳 부터 순환.
        return
    else:
        dfs(num)


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if visited[i] == False:
            cycle = []
            dfs(i)

    print(n - len(ans))
