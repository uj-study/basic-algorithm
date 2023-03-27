n, m = map(int, input().split())

# 최대 공약수
def GCD(a, b):
  if a % b == 0:
    return b
  else:
    return GCD(b, a % b)

def LCM(a, b):
  return (a * b) // GCD(a, b)

# 더 큰 수가 첫번째 인자로 들어가게하기 위함.
if n < m: 
  n, m = m, n

print(GCD(n, m))
print(LCM(n, m))
