import sys
input = sys.stdin.readline

n,c  = map(int,input().split())
locations = []
for i in range(n):
    locations.append(int(input().rstrip()))
locations.sort()

start = 1
end = locations[-1] - locations[0]
result = 0

while start <= end:
    mid = (start + end)//2
    cnt = 1
    now = locations[0]  # 처음 설치된 공유기의 위치
    for i in range(n):  # 공유기 설치가능하면 cnt증가
        if locations[i] - now >= mid:
            cnt += 1
            now = locations[i]

    if cnt >= c:    # 넘어가면 여러개 가능
        result = mid
        start = mid + 1

    else: 
        end = mid-1

print(result)