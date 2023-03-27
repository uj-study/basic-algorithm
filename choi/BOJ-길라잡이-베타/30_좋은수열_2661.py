import sys
input = sys.stdin.readline

n = int(input())

def func(num, idx):
    for i in range(1, idx//2+1):    # 좋은 수열인지 검사
        if num[idx-(2*i):idx-(2*i)+i] == num[idx-(2*i)+i :]:
            return
    
    if idx == n:    # n 자리의 수열 다 만들면 출력
        print(*num, sep='')
        exit()

    for a in [1, 2, 3]:
        if num and num[-1] == a:    # 마지막 숫자 동일하면 넣지X
            continue
        num.append(a)   # 마지막 숫자 동일하지X 넣음
        func(num, idx+1)
        num.pop()

func([],0)
