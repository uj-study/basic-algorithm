import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []

home = []
chicken = []

result = 1e9

for i in range(N):
  data = list(map(int, sys.stdin.readline().split()))
  city.append(data)


for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      home.append([i, j])
    elif city[i][j] == 2:
      chicken.append([i, j])

for chi in combinations(chicken, M):
  tmp = 0
  for h in home:
    chicken_far = 1e9
    for c in chi:
      chicken_far = min(chicken_far, abs(h[0] - c[0]) + abs(h[1] - c[1]))
    tmp += chicken_far
  result = min(result, tmp)

print(result)