import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a = list(input().rstrip())
    sum = 0
    for i in a:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')