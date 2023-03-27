import sys

t = int(sys.stdin.readline())

return_zero = [1, 0, 1] + [0] * 38
return_one = [0, 1, 1] + [0] * 38

def fibonacci(num):
    if num >= 3:
        for i in range(3, num+1):
          return_zero[i] = return_zero[i-1] + return_zero[i-2]
          return_one[i] = return_one[i-1] + return_one[i-2]

    print(return_zero[num], return_one[num])

for i in range(t):
    n = int(sys.stdin.readline())
    fibonacci(n)
