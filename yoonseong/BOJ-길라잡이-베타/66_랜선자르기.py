import sys

K, N = map(int, sys.stdin.readline().split())
lines = []

for i in range(K):
    lines.append(int(sys.stdin.readline()))

start, end = 1, max(lines)

while start <= end:
    count = 0
    mid = (start + end) // 2

    for l in lines:
        count += l // mid # 몫을 더해줌. (l이 mid 보다 큰 경우를 따질 것 없이)
    
    if count >= N:
       start = mid + 1
    else:
       end = mid - 1

print(end)
