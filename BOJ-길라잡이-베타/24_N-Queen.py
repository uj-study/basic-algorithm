# 기본 가정: 같은 행에는 퀸을 놓지 않는다.
# Promising: 기존에 놓인 것들과 같은 열이나 같은 대각선에 놓이는지를 확인
# col[i] : i번째 행에서 퀸이 놓여져있는 열의 위치

# 유망 조건
# 1. 열 체크 => col[i] == col[k]: 같은 열에 놓이게 되므로 유망하지 않음
# 2. 대각선 체크
# 왼쪽 대각선 : 열에서의 차이와 행에서의 차이가 같다. => col[i] - col[k] == i - k
# 오른쪽 대각선 : 열에서의 차이와 행에서의 차이의 마이너스가 같다 => col[i] - col[k] == k - i
import sys
n = int(sys.stdin.readline().rstrip())

result = 0
col = [0] * n

def is_possible(x):
  for i in range(x): # 이전 행들까지 체크
    if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
      return False
  
  return True

def n_queen(x):
  global result

  if x == n:
    result += 1
    return
  else:
    for i in range(n):
      # [x, i]에 퀸을 놓겠다.
      col[x] = i
      if is_possible(x):
        # print(x, col)
        n_queen(x + 1)

n_queen(0)
print(result)