import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr=[]

for i in range(1,n+1):
    if i == 1:
        continue

    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break

    else:
        arr.append(i)

cnt = 0
start = 0
end = 0
while end <= len(arr):
    temp_sum = sum(arr[start:end])  # 연속된 소수의 합
    if temp_sum == n:   # n과 같으면 cnt 추가
        cnt += 1
        end += 1    
    elif temp_sum < n:
        end += 1
    else:
        start += 1

print(cnt)