import sys
from collections import deque
n = int(sys.stdin.readline())
d = deque()

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push_front':
        d.appendleft(a[1])
    elif a[0] == 'push_back':
        d.append(a[1])
    elif a[0] == 'pop_front':
        if len(d) == 0:
            print('-1')
        else : 
            print(d[0]) 
            d.popleft()
    elif a[0] == 'pop_back':
        if len(d) == 0:
            print('-1')
        else : 
            print(a[len(d)-1])
            d.pop()
    elif a[0] == 'size':
        print(len(d))
    elif a[0] == 'empty':
        if len(d) == 0:
            print('1')
        else:
            print('0')
    elif a[0] == 'front':
        if len(d) == 0:
            print('-1')
        else:
            print(d[0])
    elif a[0] == 'back':
        if len(d) == 0:
            print('-1')
        else:
            print(d[len(d)-1])