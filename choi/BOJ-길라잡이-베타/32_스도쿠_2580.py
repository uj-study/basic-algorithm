import sys
input = sys.stdin.readline

arr = []

for i in range(9):
    arr.append(list(map(int,input().rstrip().split())))

blank = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))

def chk_row(n, x):  # 열방향 체크 (중복이면 False 반환)
    for i in range(9):
        if arr[x][i] == n:
            return False
    return True

def chk_col(n, y):  # 행방향 체크 (중복이면 False 반환)
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True

def chk_rec(x, y, n):   # 3*3 체크 (중복이면 False 반환)
    x = x//3*3
    y = y//3*3
    for i in range(3):
        for j in range(3):
            if arr[x+i][y+j] == n:
                return False
    return True

def dfs(cnt):   # 스도쿠 채우기
    if cnt == len(blank):   # cnt가 0의 개수만큼 커지면
        for i in range(9):  # 출력
            print(*arr[i],end=' ')  
            print()
        exit()
    
    x = blank[cnt][0]   # 0의 x좌표
    y = blank[cnt][1]   # 0의 y좌표

    for i in range(1,10):
        # 세가지 조건에 만족하면
        if chk_col(i, y) and chk_rec(x, y, i) and chk_row(i, x):    
            arr[x][y] = i   # 입력
            dfs(cnt+1)  # 다음 0인 좌표로 이동
            arr[x][y] = 0   # 초기화

dfs(0)
