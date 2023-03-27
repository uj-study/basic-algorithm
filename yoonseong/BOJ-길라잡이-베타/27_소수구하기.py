import sys
import math

M, N = map(int, sys.stdin.readline().split())

def is_Prime(n):
  if n == 1:
    return False
    
  for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False
    
  return True

for i in range(M, N+1):
  if is_Prime(i):
    print(i)
