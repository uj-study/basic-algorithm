import sys

N = int(input())

parenthesis_Arr = []

for _ in range(N):
  parenthesis_Arr.append(sys.stdin.readline().rstrip())

def isVPS(str):
  if len(str) % 2 == 1:
    return 'NO'

  count = 0
  left_stack = []

  for s in str:
    if s == '(':
      left_stack.append('(')
    else: # ')' 일 경우
      if len(left_stack) == 0:
        return 'NO'
      else:
        left_stack.pop()
        count += 1
    
  if count == len(str)//2 and len(left_stack) == 0:
      return 'YES'
  else:
    return 'NO'
  
for str in parenthesis_Arr:
  print(isVPS(str))

