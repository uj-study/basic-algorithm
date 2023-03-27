T = int(input())

def make_N(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return make_N(n-1) + make_N(n-2) + make_N(n-3)

for i in range(T):
  n = int(input())
  print(make_N(n))