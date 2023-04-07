import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    nums[i] = max(nums[i-1] + nums[i], nums[i])

print(max(nums))
