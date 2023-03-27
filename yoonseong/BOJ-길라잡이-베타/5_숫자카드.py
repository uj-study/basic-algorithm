import sys

N = int(input())
data_N = list(map(int,sys.stdin.readline().split()))
data_N.sort()

M = int(input())
data_M = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) //2

    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid -1
  return 0

for m in data_M:
  print(binary_search(data_N, m, 0, len(data_N) - 1))