N, K = map(int, input().split())

num_list = [i for i in range(1, N+1)] # 배열에 숫자 순서대로 삽입 

idx = 0
result = []

for _ in range(N):
  idx += K-1

  if idx >= len(num_list):
    idx = idx % len(num_list)
  result.append(str(num_list.pop(idx))) # join을 위해 형변환

print("<", ", ".join(result), ">", sep="")



# 실패

# from collections import deque

# N, K = map(int, input().split())

# num_list = deque([i for i in range(1, N+1)])

# def Josephus(arr, n, k):
#   result = []

#   while len(result) != n:         # 결과의 길이가 N과 같아질 때 까지 반복.  
#     if len(arr) >= k:             # 길이가 k보다 크면 k-1만큼 앞에서 빼고 뒤에 넣어줌. 
#       for i in range(k-1):
#         arr.append(arr.popleft())
#       result.append(arr.popleft())
#     else:                        # 길이가 짧아졌을 때 경우가 틀림
#       for i in range(k):
#           arr.append(arr.popleft())
#       if len(arr) % 2 == 1:       # arr 길이가 홀수
#         result.append(arr.popleft())
#       else:                       # arr 길이가 짝수
#         result.append(arr.pop())
    
#     print('result', result)


# Josephus(num_list, N, K)

