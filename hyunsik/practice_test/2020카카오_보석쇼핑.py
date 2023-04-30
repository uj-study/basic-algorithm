def solution(gems):
    dt = {}
    for i in range(len(gems)):
        if dt.get(gems[i]):
            dt[gems[i]][0] = min(dt[gems[i]][0], i)
            dt[gems[i]][1] = max(dt[gems[i]][1], i)
        else:
            dt[gems[i]] = [i, i] # 최소와 최대만 저장
    ans_0 = 100001
    ans_1 = 0
    for _, x in dt.items():
        ans_0 = min(ans_0, x[1])
        ans_1 = max(ans_1, x[0])
    
    return [ans_0 + 1, ans_1 + 1]

print(solution(["AA", "AB", "AC", "AA", "AC"]))