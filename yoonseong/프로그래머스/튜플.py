def solution(s):
    answer = []
    
    nums = []
    elements = s[1:-1]

    idx = 0 

    while idx < len(elements):
        if elements[idx] == '{':
            num = []
            idx += 1
            while elements[idx] != '}':
                num.append(elements[idx])
                idx += 1
            nums.append(num)
        idx += 1

    arr = []

    for n in nums:
        arr.append("".join(n).split(','))

    arr.sort(key=len)

    for a in arr:
        for e in a:
            if int(e) not in answer:
                answer.append(int(e))
    return answer
