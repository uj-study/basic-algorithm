import sys
input = sys.stdin.readline

n = int(input())
budgets = sorted(list(map(int, input().split())))
max_budget = int(input())

start = 0
end = max(budgets)

while start <= end:
    mid = (end + start) // 2
    tmp = 0   # 임시 총액

    for budget in budgets:  # 조건대로 총액에 더함
        if budget > mid: 
            tmp += mid
        else:
            tmp += budget

    if tmp <= max_budget:  # start 높여서 탐색
        start = mid + 1
    else:   # end 낮춰서 탐색
        end = mid - 1 
        
print(end)

