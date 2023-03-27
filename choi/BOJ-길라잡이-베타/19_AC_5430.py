import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    flag = 0
    order = input().rstrip()
    no = int(input())
    list = deque(input().rstrip()[1:-1].split(','))
    
    if no == 0:
        list=[]
    
    for j in order:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if list:
                if flag % 2 == 0:
                    list.popleft()
                else:
                    list.pop()
            else:
                print('error')
                break
    

    else:
        if flag % 2 == 1:
            list.reverse()
        print('['+','.join(list)+']')

