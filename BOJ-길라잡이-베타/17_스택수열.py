import sys

n = int(input())

nums = []
result = []
current = 1
isValid = True

for i in range(n):
  data = int(sys.stdin.readline())
  while current <= data:
    nums.append(current)
    result.append('+')
    current += 1
  
  if nums[-1] == data:
    nums.pop()
    result.append('-')
  else:
    isValid = False

if isValid:
  for r in result:
    print(r)
else:
  print('NO')
