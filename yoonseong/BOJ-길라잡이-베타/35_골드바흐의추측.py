# pypy로 정답처리
import sys

max = 1000000
prime_list = [True for _ in range(1000001)]

for i in range(2, 1001):
  if prime_list[i]:
    for j in range(i + i, 1000001, i):
      prime_list[j] = False
  
while True:
  n = int(sys.stdin.readline())
  flag = False

  if n == 0:
    break
  
  for i in range(3, 1000001):
    if prime_list[i]:
      if prime_list[n - i]:
        flag = True
        print(n, "=", i, "+", n-i)
        break
  
  if (not flag):
    print("Goldbach's conjecture is wrong.")
