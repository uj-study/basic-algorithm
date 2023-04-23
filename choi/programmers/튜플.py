def solution(s):
    sList = s[2:-2].split('},{')
    sList.sort(key=lambda x: len(x))
    last_index = len(sList[-1])//2+1
    for i in range(len(sList)):
        sList[i] = sList[i].split(',')
    ans=[]
    for i in sList[-1]:
        if i != ',':
            for j in range(len(sList)):
                if i in sList[j]:
                    ans.append(int(i))
    count_ans = {}
    for i in ans:
        count_ans[i] = count_ans.get(i,0)+1

    result = sorted(count_ans, key=count_ans.get,reverse=True)
    
    answer = []
    return result