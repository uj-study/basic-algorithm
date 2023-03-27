# 최대공약수
def GCD(n, m): # n에 항상 더 큰 수를 대입
  if n % m == 0:
    return m
  else:
    return GCD(m, n % m)

# 최소공배수
def LCM(n, m):
  return (n * m) // GCD(n, m) 

print(GCD(24,8), LCM(24, 8))

