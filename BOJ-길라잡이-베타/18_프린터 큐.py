import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num, index = map(int,input().split())
    order = deque(list(map(int, input().split())))
    no = 0
    
    while order:
        primary = max(order)
        first = order.popleft() 
        index -= 1

        if primary == first:
            no += 1
            if index < 0:
                print(no)
                break
        
        else:
            order.append(first)
            if index < 0:
                index = len(order) - 1

    