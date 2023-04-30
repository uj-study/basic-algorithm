from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

# 가능한지 체크하는 함수
def isPossible(target, banned_id): 
    for i in range(len(banned_id)):
        if len(target[i]) != len(banned_id[i]): # 두 사용자 이름의 길이가 다르면 가능하지 않음
            return False
        for j in range(len(target[i])):
            if banned_id[i][j] == '*': # *로 된 부분은 아무 문자나 올 수 있으므로 continue
                continue
            if target[i][j] != banned_id[i][j]: # *이 아닌 부분의 문자가 다르면 대상이 될 수 없음
                return False
    return True


def solution(user_id, banned_id):
    answer = []

    for target in permutations(user_id, len(banned_id)): # 불량 사용자 길이만큼의 순열생성
        # 순열을 순회하며 체크
        if isPossible(target, banned_id):
            target = set(target)
            if target not in answer:
                answer.append(target)

    return len(answer)

print(solution(user_id, banned_id))
