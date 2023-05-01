numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    answer = ''

    # 각 번호의 좌표
    position = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    } 

    current_left = (3, 0) # 현재 왼손가락 위치 (시작위치로 초기화)
    current_right = (3, 2) # 현재 오른손가락 위치 (시작위치로 초기화)

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            current_left = position[n]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            current_right = position[n]
        else:
            diff_L = abs(position[n][1] - current_left[1]) + abs(position[n][0] - current_left[0]) # 눌러야 할 버튼과 현재 왼손가락 위치의 거리 차이
            diff_R = abs(position[n][1] - current_right[1]) + abs(position[n][0] - current_right[0]) # 눌러야 할 버튼과 현재 오른손가락 위치의 거리 차이

            if diff_L < diff_R: # 왼손이 더 가까우면
                answer += 'L'
                current_left = position[n]
            elif diff_L > diff_R: # 오른손이 더 가까우면
                answer += 'R'
                current_right = position[n]
            else: # 거리가 같으면 어느 손잡이냐에 따라 누름
                if hand == 'right':
                    answer += 'R'
                    current_right = position[n]
                else:
                    answer += 'L'
                    current_left = position[n]
                    
    return answer

print(solution(numbers, hand))
