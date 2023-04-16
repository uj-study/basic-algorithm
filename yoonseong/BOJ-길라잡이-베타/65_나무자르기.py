import sys 

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for t in trees:
        if t > mid:
            total += t - mid
    
    if total >= M: # 원하는 길이보다 많이 남으면 더 많이 잘라야함
        start = mid + 1
    else: # 원하는 길이보다 작으면 더 적게 잘라야함
        end = mid - 1

print(end)
