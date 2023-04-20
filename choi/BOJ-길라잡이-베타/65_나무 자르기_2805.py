import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = sorted(list(map(int,input().split())))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (end + start) // 2

    total = 0   # 나무의 총 길이
    for i in tree:
        if i > mid: # 조건 만족하면 총길이에 더함
            total += (i-mid)

    if total == m:  # 목표 채우면 종료
        result = mid
        break
    elif total < m: # 목표에서 남았으면 최대길이 낮추기
        end = mid -1
    else:   # 과하면 최소길이 높이기
        result = mid
        start = mid + 1

print(result)
