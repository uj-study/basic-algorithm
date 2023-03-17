import sys
input = sys.stdin.readline

# 소수판정
def is_prime(value) :
    if value > max_value :
        for prime in primes :
            if prime >= value :
                break
            elif value % prime == 0 :
                return False

        return True
    else :
        return data[value]

# 에라토스테네스의 체
max_value = int((2*10^12)**0.5) # 최대의 제곱근까지 
data = [False, False] + [True for _ in range(max_value-1)]
primes = [] # 소수 목록
for i in range(2, max_value + 1) :
    if data[i] :
        primes.append(i)    # True 면 소수 목록에 추가
        for j in range(i+i, max_value, i) : # i의 배수는 False로 바꾸기
            data[j] = False

# 구현
T = int(input())
for _ in range(T):
    S = sum(map(int,input().split()))
    if S < 4:
        print('NO')
    elif S % 2 == 0:
        print('YES')
    elif is_prime(S-2):
        print('YES')
    else:
        print('NO')