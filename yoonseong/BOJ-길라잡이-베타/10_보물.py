import sys

N = int(input())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

answer = 0

for i in range(N):
  minA = a.pop(a.index(min(a)))
  maxB = b.pop(b.index(max(b)))
  answer += (minA  * maxB)

print(answer)
