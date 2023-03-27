import sys
from itertools import combinations

N, S = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))

result = 0

for i in range(1, N+1):
  num_list_comb = list(combinations(num_list, i))

  for n in num_list_comb:
    if sum(n) == S:
      result += 1

print(result)
