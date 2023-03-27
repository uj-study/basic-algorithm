import sys
from itertools import combinations
# TODO 라이브러리가 아닌 dfs, bfs 방식 찾아보기

while True:
  arr = sys.stdin.readline().split()

  if arr[0] == '0':
    break

  else:
    k = arr[0]
    S = arr[1:]

    result = list(combinations(S, 6))

    for r in result:
      r_list = list(r)
      print(" ".join(r_list))
    print()
