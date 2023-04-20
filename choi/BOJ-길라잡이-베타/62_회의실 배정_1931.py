import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

a = sorted(a, key=lambda x: x[0])   # 시작시간 정렬
a = sorted(a, key=lambda x: x[1])   # 끝나는 시간 정렬

last=0  # 전 회의 끝나는 시간
cnt=0   # 회의 수

for i, j in a:
    if i>=last: # 시작시간이 전 회의의 끝나는 시간이상
        cnt+=1  # 회의 수 증가
        last=j  # 끝시간 갱신

print(cnt)