import sys

N = int(input())

duplicate_arr = list(map(int, sys.stdin.readline().split()))

remove_duplicate_arr = list(set(duplicate_arr))

remove_duplicate_arr.sort()

for a in remove_duplicate_arr:
  print(a, end = " ")