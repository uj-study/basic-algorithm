import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [0] * (k+1)
dp[0] = 1 # 가진 동전 하나로 k원을 만드는 경우를 위해 1로 설정

for i in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in coins:
    for i in range(coin, k+1): # i - coin이 양수일 때만 따지기위해 coin부터 반복.
       dp[i] += dp[i - coin]

print(dp[k])
