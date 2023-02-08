import sys

N = int(input())

N_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

dict = {}

for n in N_list:
  if n in dict:
    dict[n] += 1
  else:
    dict[n] = 1

for m in M_list:
  result = dict.get(m)

  if result == None:
    print(0, end = " ")
  else:
    print(result, end = " ")

# 틀린 풀이 (체크해보기/ 이분탐색 풀어보기)
# MAX_NUM = 10000000
# tmp_list = [0 for i in range(2 * MAX_NUM + 1)]

# N = int(input())

# N_list = list(map(int, sys.stdin.readline().split()))

# M = int(input())
# M_list = list(map(int, sys.stdin.readline().split()))

# for n in N_list:
#   if n > 0:
#     tmp_list[MAX_NUM + n] += 1
#   else:
#     tmp_list[n] += 1

# result = []
# for m in M_list:
#   if m > 0:
#     result.append(tmp_list[MAX_NUM + m])
#   else:
#     result.append(tmp_list[m])

# for r in result:
#   print(r, end = " ")

