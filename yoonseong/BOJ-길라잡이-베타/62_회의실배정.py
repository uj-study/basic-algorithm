import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    arr.append([start, end])

# 회의가 먼저 끝나는 순으로 정렬 
arr = sorted(arr, key = lambda a : a[0]) # 시작이 빠른 순 정렬
arr = sorted(arr, key = lambda a : a[1]) # 종료가 빠른 순 정렬

prev_end = arr[0][1] # 이전 회의 종료시간, 첫번째 삽입
answer = 1

for i in range(1, N):
    if arr[i][0] >= prev_end: # 이전 회의 종료시간보다 다음 회의 시작시간이 크거나 같으면
        answer += 1
        prev_end = arr[i][1]

print(answer)
