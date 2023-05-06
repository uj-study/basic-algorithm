from itertools import permutations

expression = "100-200*300-500+20"

def makeExp(expression):
    i = 0
    exp = []

    while True:
        num = ''
        # 숫자라면
        while i < len(expression) and expression[i] != '*' and expression[i] != '+' and expression[i] != '-':
            num += expression[i]
            i += 1
        exp.append(int(num))

        if i >= len(expression):
            break

        # 연산자라면
        if expression[i] != '*' or expression[i] != '+' or expression[i] != '-':
            exp.append(expression[i])
            i += 1
    return exp


def solution(expression):
    exp = makeExp(expression)
    oper_per = list(permutations(['*', '+', '-'], 3))  # 연산자 우선순위 순열
    answer = 0
    for oper in oper_per:
        exp_copy = exp.copy()
        for op in oper: # 우선순위에 따라 연산자 계산 
            exp_len = len(exp_copy)
            i = 0
            while i < exp_len: # 식 탐색
                if exp_copy[i] == op: # 연산자라면
                    if op == '-':
                        exp_copy[i] = exp_copy[i - 1] - exp_copy[i + 1]
                    elif op == '+':
                        exp_copy[i] = exp_copy[i - 1] + exp_copy[i + 1]
                    elif op == '*':
                        exp_copy[i] = exp_copy[i - 1] * exp_copy[i + 1]
                    del exp_copy[i - 1] # 연산에 사용된 것 제거
                    del exp_copy[i] # 연산에 사용된 것 제거
                    exp_len -= 2 # 연산에 사용된 것들 만큼 길이에서 제거 (피연산자 2개와 연산자 1개를 사용하면 결과값을 제외하고 길이2 제거)
                else: # 연산자가 아니면 인덱스 + 1
                    i += 1
        answer = max(answer, abs(exp_copy[0]))

    return answer

print(solution(expression))
