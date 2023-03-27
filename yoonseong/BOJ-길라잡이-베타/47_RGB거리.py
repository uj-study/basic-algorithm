import sys

N = int(sys.stdin.readline())
house = []

for i in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0] # 빨간집을 선택한 경우, 이전에 초록, 파란색으로 색칠한 값 중 작은 값을 더해서 저장
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1] # 초록집을 선택한 경우, 이전에 빨강, 파란색으로 색칠한 값 중 작은 값을 더해서 저장   
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2] # 파란집을 선택한 경우, 이전에 빨강, 초록색으로 색칠한 값 중 작은 값을 더해서 저장 

print(min(house[N-1]))
