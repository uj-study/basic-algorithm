import sys

N = int(input())

cmd_list = []

for _ in range(N):
  data = list(sys.stdin.readline().split())
  cmd_list.append(data)

dummy = []
result = []

def stack(arr, i):
  if arr[i][0] == 'push':
    dummy.append(int(arr[i][1]))
  elif arr[i][0] == 'pop':
    if len(dummy) > 0:
      result.append(dummy.pop())
    else:
      result.append(-1)
  elif arr[i][0] == 'size':
    result.append(len(dummy))
  elif arr[i][0] == 'empty':
    if len(dummy) > 0:
      result.append(0) 
    else:
      result.append(1)
  elif arr[i][0] == 'top':
    if len(dummy) > 0:
      result.append(dummy[len(dummy) - 1])
    else:
      result.append(-1)

for i in range(N):
  stack(cmd_list, i)

for i in result:
  print(i)