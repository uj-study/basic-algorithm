import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)

if n == 1:
   print(cards[0])
else:
  dp[1] = cards[0]
  for i in range(2, n+1):
    tmp = -1
    # 카드 i개를 만드는 최댓값을 저장하는 배열에 값 저장.
    # i의 절반까지 돌며 체크
    # ex) i가 6인 경우, (1, 5) (2, 4) (3, 3) (4, 2) (5, 1)의 경우가 나오지만 뒤의 경우는 앞의 결과와 같으므로 굳이 반복 할 필요가 없다.
    for j in range(1, i//2 + 1):
      tmp = max(tmp, dp[j] + dp[i-j])
    # 가격 1을 i 만큼 곱하는 경우, 가격자체가 i인 경우와 위의 값들 중 최댓값이 카드 i개를 만드는 최댓값
    dp[i] = max(i * cards[0], cards[i-1], tmp)
  print(dp[n])
