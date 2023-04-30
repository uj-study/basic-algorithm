import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

if M >= sum(arr): # 예산이 충분하면
    print(max(arr)) # 예산 요청 중 가장 큰 값
else:   
    start, end = 0, max(arr)

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for a in arr:
            total += min(a, mid)

        if total > M: # 예산의 합이 M(주어진 예산)보다 크면
            end = mid - 1
        else:
            start = mid + 1
    
    print(end)
