import sys
from collections import deque

testCase = int(input())

for _ in range(testCase):
  N, M = map(int, sys.stdin.readline().split())
  importance = deque(list(map(int, sys.stdin.readline().split())))

  count = 0

  while importance:
    MAX_IMPORTANCE = max(importance)
    first = importance.popleft()
    M -= 1 # 핵심

    if first == MAX_IMPORTANCE:
      count += 1
      if M < 0: # 핵심
        print(count)
        break
    else:
      importance.append(first)
      if M < 0: # 핵심
        M = len(importance) - 1