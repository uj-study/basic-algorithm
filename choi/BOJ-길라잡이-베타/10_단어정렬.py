import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

s_data = set(data)
l_data = list(s_data)
l_data.sort()
l_data.sort(key = len)


for i in l_data:
    print(i)