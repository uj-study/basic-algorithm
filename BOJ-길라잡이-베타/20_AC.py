import sys
from collections import deque

def AC(cmd, arr):
  flag = 0
  for c in cmd:
    if c == 'R':
      flag += 1
    elif c == 'D':
      if len(arr) > 0:
        if flag % 2 == 0:
          arr.popleft()
        else:
          arr.pop()
      else:
        print('error')
        return
  
  if flag % 2 == 0:
    print("[" + ",".join(arr) + "]")
  else:
    arr.reverse()
    print("[" + ",".join(arr) + "]")

T = int(input())

for i in range(T):
  command = sys.stdin.readline().rstrip()
  n = int(input())
  arr = deque(sys.stdin.readline().strip()[1:-1].split(','))

  if n == 0:
    arr = []
  

  AC(command, arr)

