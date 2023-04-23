# 시간초과

def solution(stones, k):
    answer = 0

    stone_len = len(stones)

    now = -1
    jump = 1

    while True:
        try:
            if stones[now+jump]:
                stones[now+jump] -= 1
                now = now+jump
                jump = 1
            else:
                if jump == k:
                    break
                jump += 1
        except:
            answer += 1
            now = -1
            jump = 1


    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))