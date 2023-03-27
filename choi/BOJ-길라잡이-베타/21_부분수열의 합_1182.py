from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int,input().split())
a = list(map(int,input().split()))
count = 0

for no in range(1, N+1):
    a_com = combinations(a, no)
    
    for i in a_com:
        if sum(i) == S:
            count += 1

print(count)