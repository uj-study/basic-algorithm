import re

def solution(expression):
    numbers = re.split('[^0-9]',expression)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    sign = [c for c in expression if not c.isalnum()]


    answer = 0
    return answer

print(solution("100-200*300-500+20"))