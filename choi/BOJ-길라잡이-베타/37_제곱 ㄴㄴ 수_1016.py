import sys
input = sys.stdin.readline

min, max = map(int,input().split())


def func(min, max):
    ans = max - min + 1
    arr = [False]*(max-min+1)   # 제곱의 배수가 아닌 수 False
    for i in range(2, int(max**0.5+1)): 
        sqrt = i**2
        for j in range((((min-1)//sqrt)+1)*sqrt,max+1,sqrt):    # 제곱수의 배수 
            if not arr[j-min]:
                arr[j-min] = True
                ans -= 1
    print(ans)

func(min,max)
    