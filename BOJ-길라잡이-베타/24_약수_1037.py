import sys
input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
print(min(list)*max(list))