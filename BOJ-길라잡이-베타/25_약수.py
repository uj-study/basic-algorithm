import sys

N = int(input())

divisor_list = list(map(int, sys.stdin.readline().split()))

min_divisor = min(divisor_list)
max_divisor = max(divisor_list)

print(min_divisor * max_divisor)
  