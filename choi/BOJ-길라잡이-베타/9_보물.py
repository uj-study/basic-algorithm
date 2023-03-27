import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a.sort()

result = 0
for i in range(n):
    result += a[i]*max(b)
    b.remove(max(b))
print(result)