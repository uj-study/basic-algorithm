import sys

N = int(sys.stdin.readline())

gap_list = []
result = 0

tmp = int(sys.stdin.readline().rstrip())

for i in range(N-1):
  data = int(sys.stdin.readline().rstrip())
  gap = data - tmp
  gap_list.append(gap)
  tmp = data

def GCD(a, b):
  while b:
    a, b = b, a%b
  return a

gcd = gap_list[0]
for i in range(1, len(gap_list)):
  gcd = GCD(gcd, gap_list[i])

for g in gap_list:
  result += g // gcd - 1

print(result)

# 시간초과
# for i in range(trees[0], trees[-1], gcd): # 나무들의 간격들의 최대공약수를 구한 뒤, 그 간격마다 존재유무 체크
#   if i not in trees:
#     result += 1
