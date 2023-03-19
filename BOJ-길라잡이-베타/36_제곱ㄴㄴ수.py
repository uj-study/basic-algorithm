import sys

input = sys.stdin.readline

a, b = map(int, input().split())

sosu = [True]*1000001000001

four = 4
while four < 1000001000001:
    sosu[four] = False
    four += 4

for x in range(2, 10**11 + 1):
    k = 2*x - 1
    while k < 1000001000001:
        sosu[k] = False
        k += 2*x -1

print(sosu[:20])