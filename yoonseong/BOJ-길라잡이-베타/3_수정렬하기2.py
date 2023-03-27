import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()

for i in arr:
  print(i)