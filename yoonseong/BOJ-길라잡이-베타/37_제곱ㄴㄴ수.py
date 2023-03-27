import sys
import math

min, max = map(int, sys.stdin.readline().split())
check_list = [True for _ in range(max - min + 1)]
square_list = [i*i for i in range(2, int(math.sqrt(max))+1)]

for s in square_list:
    n = min // s * s
    while n < max + 1:
        if n - min >= 0:
            check_list[n-min] = False
        n += s
print(check_list.count(True))

# 1.메모리 초과
# import sys
# import math

# min, max = map(int, sys.stdin.readline().split())
# num_list = [True for _ in range(max + 1)]

# square_list= []

# for i in range(2, int(math.sqrt(max)) + 1):
#   square_list.append(i**2)

# for square in square_list:
#   i = 1
#   while square * i <= max:
#     num_list[square * i] = False
#     i += 1

# print(num_list[min:max + 1].count(True))

# 2. 시간 초과
# import sys
# import math

# min, max = map(int, sys.stdin.readline().split())
# num_list = [i for i in range(min, max + 1)]
# except_count = 0 # 제곱ㄴㄴ가 아닌 수

# square_list= []

# for i in range(2, int(math.sqrt(max)) + 1):
#   square_list.append(i**2)

# for square in square_list:
#   i = 1
#   while square * i <= max:
#     if square * i in num_list:
#       except_index = num_list.index(square * i)
#       num_list[except_index] = False
#       except_count += 1
#     i += 1

# print(len(num_list) - except_count)