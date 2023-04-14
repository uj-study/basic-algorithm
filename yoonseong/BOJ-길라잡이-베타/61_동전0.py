import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
answer = 0

for i in range(n):
    coin = int(sys.stdin.readline())
    if coin <= k:
        coins.append(coin)

coins.reverse()

for coin in coins:
    count = k // coin
    k = k % coin

    answer += count

    if k == 0:
        break
  
print(answer)
