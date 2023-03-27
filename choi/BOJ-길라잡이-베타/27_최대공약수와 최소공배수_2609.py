import sys
input = sys.stdin.readline

a, b = map(int, input().split())

major = []
minor = []

for i in range(1,min(a,b)+1):
    if (a % i==0 and b%i==0):
        major.append(i)

for i in range(max(a,b),a*b+1):
    if (i%a==0 and i%b==0):
        minor.append(i)

print(max(major))
print(min(minor))
