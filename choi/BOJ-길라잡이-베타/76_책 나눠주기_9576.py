import sys
input = sys.stdin.readline

test = int(input())
n, m = map(int,input().split())
book_num = []
for i in range(m):
    book_num.append(list(map(int,input().split())))
    
