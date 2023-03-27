import sys

N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * 301

# 계단 2개까지는 계산
if N <= 2:
  print(sum(arr))

else: # 계단이 2개가 넘으면
  dp[0] = arr[0]
  dp[1] = arr[0] + arr[1]
  dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) # 3개라면 index가 2인 계단은 무조건 밟아야하므로

  # 3개가 초과되는 수라면 
  for i in range(3, N):
    # i번째 계단(arr[i]은 무조건 밟아야하고, 
    # 그 이전 계단(arr[i-1])을 밟을 때 ( arr[i] + arr[i-1] + 그 앞앞 계단까지의 최대값(dp[i-3]) )
    # 그 이전 계단을 밟지않을 때를 나눠서 더 큰 값을 dp에 저장
    dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2]) 
  print(dp[N-1])
