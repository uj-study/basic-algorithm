import sys

N, C = map(int, sys.stdin.readline().split())
arr = []
answer = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

start, end = 1, arr[-1] - arr[0] # 간격의 최소와 최대

while start <= end:
    count = 1 
    mid = (start + end) // 2 # 다음 설치가 가능한 위치

    current = arr[0] # 시작 좌표

    for i in range(1, N):
        gap = arr[i] - current
        if gap >= mid: # 이전과의 간격이 mid(설치가능한 위치)보다 크거나 같으면
            count += 1
            current = arr[i]

    if count < C: # 설치된 개수가 C보다 작으면 간격을 좁혀야함
        end = mid - 1
    else:
        answer = mid
        start = mid + 1 
        
print(answer)       


# 메모리 초과
# import sys
# from itertools import combinations

# N, C = map(int, sys.stdin.readline().split())
# arr = []

# for i in range(N):
#     arr.append(int(sys.stdin.readline()))
# arr.sort()

# gap = []
# for i in range(1, N):
#     gap.append(arr[i] - arr[0])

# comb = list(combinations(gap, C))

# print(min(comb[-1]))
