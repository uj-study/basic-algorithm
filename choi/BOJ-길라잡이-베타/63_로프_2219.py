import sys
input = sys.stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input().rstrip()))
rope.sort()

# 낮은 중량*개수, 큰 중량*개수 비교
new_rope = [0]*(n+1)

for i in range(n-1,-1,-1):  
    new_rope[i]=(n-i)*rope[i] 

print(max(new_rope))