import sys
input = sys.stdin.readline

n = int(input())
list = list(map(str,input().split()))
visited = [False]*10
min = ""
max = ""

def check(a,b,symbol):
    if symbol=='>':
        return a>b
    elif symbol=='<':
        return a<b

def solve(depth,s):
    global min,max

    # 처음으로 생성된게 min 마지막이 max
    if depth == n+1:
        if len(min)==0:
            min = s
        else:
            max = s
        return
    
    # 0 부터 차례로 check함수를 이용해 조건에 부합하는지 판단한 후 다음으로 이동
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1],str(i),list[depth-1]):
                visited[i] = True
                solve(depth+1,s+str(i))
                visited[i] = False

solve(0,"")
print(max)
print(min)