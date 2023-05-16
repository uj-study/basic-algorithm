import sys
input = sys.stdin.readline

test = int(input())
for i in range(test):
    n, m = map(int,input().split())
    book_num = []
    for i in range(m):
        book_num.append(list(map(int,input().split())))
    book_num.sort(key=lambda x: x[1])   # b 작은순
    # print(book_num)
    
    cnt = 0
    visited = [False]*(n+1)
    
    for a, b in book_num:
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = True
                cnt += 1
                break
    print(cnt)