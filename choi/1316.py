import sys
input = sys.stdin.readline

N = int(input())
cnt = N

for i in range(N):
    str = input().rstrip()

    for j in range(0, len(str) - 1):
        if str[j] == str[j+1]:
            pass
        elif str[j] in str[j+1:]:
            cnt -= 1
            break
print(cnt)

