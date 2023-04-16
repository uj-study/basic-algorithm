import sys
input = sys.stdin.readline

n,k = map(int,input().split())
list=[]
for i in range(n):
    list.append(int(input().rstrip()))

dp=[0 for i in range(k+1)]

dp[0] = 1

for i in list:
    for j in range(1,k+1):
        if j-i>=0:
            dp[j] += dp[j-i]

print(dp[k])