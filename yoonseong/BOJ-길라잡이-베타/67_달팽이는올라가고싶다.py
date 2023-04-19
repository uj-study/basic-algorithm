import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

# 달팽이가 days일 걸려 도착한다고 했을 때, 올라가는 횟수는 days, 내려오는 횟수는 days - 1
# V = A * days - B*(days-1) 
days = (V-B) / (A-B)

print(math.ceil(days)) # 올림
