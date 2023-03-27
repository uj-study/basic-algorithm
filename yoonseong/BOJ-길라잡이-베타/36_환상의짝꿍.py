import sys
import math

max = 2 * (10**6)
testcase = int(sys.stdin.readline())

boolean_prime_list = [True for _ in range(max + 1)]

for i in range(2, int(math.sqrt(max))+1):
    if boolean_prime_list[i]:
        for j in range(i + i, max + 1, i):
            boolean_prime_list[j]=False
prime= [i for i in range(2, max) if boolean_prime_list[i]]

for i in range(testcase):
  A, B = map(int, sys.stdin.readline().split())
  sum = A + B

  if sum < 4:
    print('NO')
  elif sum % 2 == 0: # 짝수
    print('YES')
  else: # 홀수, 홀수는 짝수 + 홀수로 만들 수 있는데 소수 중 짝수인 수가 2밖에 없으므로 해당 조건만 판단
    if sum - 2 >= max:
      flag=0
      for p in prime:
        if not (sum - 2) % p:
          flag=1
          print('NO')
          break
      if not flag:
        print('YES')
    else:
      if sum - 2 in prime:
        print('YES')
      else:
        print('NO')