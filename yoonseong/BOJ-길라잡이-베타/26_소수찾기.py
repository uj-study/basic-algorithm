import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
result = 0

def is_Prime(n):
  if n == 1:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False
  
  return True

for n in num_list:
  if is_Prime(n):
    result += 1

print(result)