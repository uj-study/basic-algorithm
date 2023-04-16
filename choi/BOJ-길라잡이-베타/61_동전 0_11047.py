import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = [int(input().rstrip()) for i in range(n)]
cnt=0
A.sort(reverse=True)

for i in A:
    cnt += k//i
    k = k%i

print(cnt)