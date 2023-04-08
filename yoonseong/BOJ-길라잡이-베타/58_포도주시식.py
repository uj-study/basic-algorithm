import sys

n = int(sys.stdin.readline())
grapes = [0]
dp = [0] * (n+1)

for i in range(n):
    grapes.append(int(sys.stdin.readline()))

if n < 3:
  print(sum(grapes))
else:
  dp[1] = grapes[1]
  dp[2] = grapes[1] + grapes[2]
  for i in range(3, n+1):
      # 해당 번째 잔을 마시냐 안마시느냐 구분
      # 마시는 경우, 3잔 연속 마시는 경우를 제외해야하므로
      # 바로 앞의 잔을 마시는 경우(dp[i-3] + grapes[i-1] + grapes[i]) => i-2번째 잔은 마실 수 없으니 i-3까지의 최댓값에 더해줌
      # 바로 앞의 잔을 안 마시는 경우(dp[i-2] + grapes[i])
      # 안 마시는 경우, 이전 잔까지의 최댓값(dp[i-1])
      dp[i] = max(dp[i-1], dp[i-2] + grapes[i], dp[i-3] + grapes[i-1] + grapes[i])
  print(dp[n])
