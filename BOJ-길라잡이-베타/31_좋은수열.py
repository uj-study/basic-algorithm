import sys

N = int(sys.stdin.readline())

def isGood(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx * 2) : -idx]: # idx ~ 마지막 인덱스 (이 길이를 diff라하면), diff길이만큼 그 이전(idx)까지의 값 비교
            return False
    else:
        return True

def solution(num):
    global N, res

    if len(num) == N:
        print(num)
        exit() # 프로그램 종료

    for i in '123':
        if isGood(num + str(i)):
            # print(num + str(i))
            solution(num + str(i))
    return

solution('1')