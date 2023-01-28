import sys
input = sys.stdin.readline

n = int(input())

a = [0]*10000

for x in range(n):
    a[int(input())-1] += 1

for y in range(10000):
    if a[y] != 0:
        for z in range(a[y]):
            print(y+1)