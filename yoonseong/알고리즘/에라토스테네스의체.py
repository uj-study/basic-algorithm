import sys
import math

M, N = map(int, sys.stdin.readline().split())
PRIME_NUM = [True for _ in range(N + 1)]
PRIME_NUM[0] = False
PRIME_NUM[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if PRIME_NUM[i] == True:
      j = 2
      while (i*j) <= N:
        PRIME_NUM[i*j] = False
        j += 1

for i in range(M, N + 1):
  if PRIME_NUM[i]:
    print(i)