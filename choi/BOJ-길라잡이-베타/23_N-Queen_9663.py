import sys
input = sys.stdin.readline

N = int(input())

ans = 0 # 경우의 수
row = [0] * N   # 체스판 배열

def able(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def disposition(y):
    global ans
    
    if y == N:
        ans += 1

    else:
        for i in range(N):
            row[y] = i

            if able(y):
                disposition(y+1)

disposition(0)
print(ans)