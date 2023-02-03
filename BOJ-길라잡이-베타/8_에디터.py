import sys

a = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
b = []

for _ in range(n):
    z = sys.stdin.readline().split()
    if z[0] == 'L':
        if a:
            b.append(a.pop())
    elif z[0] == 'D':
        if b:
            a.append(b.pop())
    elif z[0] == 'B':
        if a:
            a.pop()
    else :
        a.append(z[1])

a.extend(reversed(b))
print(''.join(a))
