import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split()))
city = list(map(int,input().split()))

first = city[0]
sum = 0
# 비교해서 갱신한 뒤 sum에 추가
for i in range(n-1):
    if city[i] < first:
        first = city[i]
    sum += first * road[i]

print(sum)