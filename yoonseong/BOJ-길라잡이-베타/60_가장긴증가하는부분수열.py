import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# arr = [0] + list(map(int, sys.stdin.readline().split()))

# dp = [0] * (n+1)
# dp[1] = 1

# for i in range(2, n+1):
#     answer = 0
#     target = arr[i]
#     for j in range(1, i):
#         if target > arr[j]:
#             answer = max(answer, dp[j])
#     dp[i] = answer + 1  # arr[i]를 마지막 값으로 갖는 가장 긴 증가하는 부분수열의 길이
        
# print(max(dp))
