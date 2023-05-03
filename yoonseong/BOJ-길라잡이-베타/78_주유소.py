import sys

N = int(sys.stdin.readline()) # 도시 수

distances = list(map(int, sys.stdin.readline().split())) # 도시 간의 거리
prices = list(map(int, sys.stdin.readline().split())) # 도시들의 주유 가격

answer = 0
min_price = prices[0] # 주유 가격이 최소인 값 저장 (처음엔 무조건 주유해야하니 첫번째 값 저장)

for i in range(N-1): # 도시사이의 간격이 있는만큼 반복
    if min_price > prices[i]: # 현재 도시의 가격이 더 작으면 min_price갱신
        min_price = prices[i]
    
    answer += distances[i] * min_price

print(answer)
