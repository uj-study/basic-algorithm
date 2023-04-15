import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int,input().split()))

dp=[list[0]]
for i in range(len(list)-1):
    dp.append(max(dp[i]+list[i+1],list[i+1]))

print(max(dp))