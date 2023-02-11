import sys
input = sys.stdin.readline

N, K = map(int,input().split())

a = []
index = 0
result = []
for i in range(N):
    a.append(i+1)

for i in range(N):
    index += K-1
    if index >= len(a):
        index = index % len(a)
    result.append(str(a.pop(index)))
print(str(result).replace('[','<').replace(']','>').replace("'",''))
