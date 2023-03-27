import sys

N = int(input())

cmd_list = []

for _ in range(N):
  data = list(sys.stdin.readline().split())
  cmd_list.append(data)

dummy = []
result = []

def queue(arr, i):
  if arr[i][0] == 'push':
    dummy.append(arr[i][1])
  elif arr[i][0] == 'pop':
    if len(dummy) > 0:
      result.append(dummy.pop(0))
    else:
      result.append(-1)
  elif arr[i][0] == 'size':
    result.append(len(dummy))
  elif arr[i][0] == 'empty':
    if len(dummy) > 0:
      result.append(0)
    else:
      result.append(1)
  elif arr[i][0] == 'front':
    if len(dummy) > 0:
      result.append(dummy[0])
    else:
      result.append(-1)
  elif arr[i][0] == 'back':
    if len(dummy) > 0:
      result.append(dummy[-1])
    else:
      result.append(-1)

for i in range(N):
  queue(cmd_list, i)

for i in result:
  print(i)