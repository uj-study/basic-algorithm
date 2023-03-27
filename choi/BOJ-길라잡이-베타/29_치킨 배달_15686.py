import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# 집과 치킨집의 좌표 
house = []
chicken = []

result = 1e9

# 집과 치킨집의 좌표 설정 
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])

# m개의 치킨집 경우의 수
for i in combinations(chicken, m):
    temp = 0    # 치킨 거리
    for j in house: # 집집마다의
        distance = 99999    
        for k in range(m):  # 모든 치킨집과의 거리 distance 구하기
            distance = min(distance,abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        temp += distance    # 도시의 치킨 거리 = 집집마다의 distance 누적
    result = min(result,temp)
print(result)

