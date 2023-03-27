import sys

N = int(input())
dummy_arr = [0] * 10001

for _ in range(N):
  t = int(sys.stdin.readline())
  dummy_arr[t] += 1

for i in range(len(dummy_arr)):
  if dummy_arr[i] > 0:
    for j in range(dummy_arr[i]):
      print(i)