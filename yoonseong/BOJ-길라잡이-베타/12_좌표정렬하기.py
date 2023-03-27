import sys

N = int(input())

points = []

for _ in range(N):
  point = list(map(int, sys.stdin.readline().split()))
  points.append(point)
  
points.sort(key=lambda x: x[1])
points.sort()

for i in points:
  print(f"{i[0]} {i[1]}")
