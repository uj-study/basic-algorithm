import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(set(a))

for i in sorted(b):
    print(i, end=' ')
