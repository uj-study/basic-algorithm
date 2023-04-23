s="{{1,2,311},{2,1},{1,2,4,311},{2}}"

sList = s[2:-2].split('},{')
sList.sort(key=lambda x: len(x))
last_index = len(sList[-1])//2+1

for i in range(len(sList)):
    sList[i] = sList[i].split(',')
print(sList)
ans=[]
for i in sList[-1]:
    if i != ',':
        print(int(i))
        for j in range(len(sList)):
            if i in sList[j]:
                ans.append(int(i))
count_ans = {}
for i in ans:
    count_ans[i] = count_ans.get(i,0)+1

result = sorted(count_ans, key=count_ans.get,reverse=True)
print(result)

# ans.sort(key=lambda x: count_ans[x])
# print(ans)
# for i in range(1,len(ans)):
#     if ans[i]==ans[i-1] :
#         ans.pop(i)
# print(ans)
                
# ans[0] = str(sList[0])
# for i in range(1,last_index):
#     sList[i] = sList[i].replace(',','')
#     #ans.append(str(set(sList[i])-set(sList[i-1])).replace('{','').replace('}','').replace("'",''))
#     ans[i] = str(set(sList[i])-set(sList[i-1]))
# print(ans)


#for i in range(len(sList)):
