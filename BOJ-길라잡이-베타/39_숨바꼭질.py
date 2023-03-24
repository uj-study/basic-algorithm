import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

if n <= k:
    print(k - n)
    exit()

