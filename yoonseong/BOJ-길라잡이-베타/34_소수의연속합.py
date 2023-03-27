import sys
import math

N = int(sys.stdin.readline())

isPrime_list = [True] * (N + 1)
prime_nums = []

for i in range(2, int(math.sqrt(N) + 1)):
  if isPrime_list[i]:
    j = 2
    while i*j <= N:
      isPrime_list[i*j] = False
      j += 1

for i in range(2, len(isPrime_list)):
  if isPrime_list[i]:
    prime_nums.append(i)

end = 0
sum = 0 # 구간의 합
result = 0

for start in range(len(prime_nums)):
  while sum < N and end < len(prime_nums):
    sum += prime_nums[end]
    end += 1
  
  if sum == N:
    result += 1
  
  sum -= prime_nums[start]

print(result)

