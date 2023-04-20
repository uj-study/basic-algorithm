import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lan = []
for i in range(k):
    lan.append(int(input().rstrip()))

start = 1
end = max(lan)

while start <= end:
    mid = (end + start) // 2
    cnt = 0   # 목표치

    for i in lan:
        cnt += i//mid

    if cnt >= n:    # 이상이면 출발 지점 높이기 
        start = mid+1
        
    else:   # 미만이면 끝 지점 낮추기
        end = mid-1

print(end)
