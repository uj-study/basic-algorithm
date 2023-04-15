import sys
input = sys.stdin.readline

n = int(input())
v = [0]
for i in range(n):
    v.append(int(input().rstrip()))

dp = [0]
dp.append(v[1])
if n>1:
    dp.append(v[1]+v[2])

for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-3]+v[i-1]+v[i],dp[i-2]+v[i]))

print(dp[n])