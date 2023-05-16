import sys
input = sys.stdin.readline

k, n = map(int,input().split())
nums = []

def func_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a = int(nums[i] + nums[j])
            b = int(nums[j] + nums[i])
            
            if a < b:
                nums[i], nums[j] = nums[j], nums[i]

for i in range(k):
    nums.append(input().rstrip())

maximum = str(max(map(int, nums)))

for i in range(k, n):
    nums.append(maximum)

func_sort(nums)

print(''.join(nums))