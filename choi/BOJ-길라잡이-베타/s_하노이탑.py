import sys

n = int(sys.stdin.readline())

def asd(a, b, c, n):
    if n == 1:
        print(a, c)
        return

    asd(a,c,b,n-1)
    print(a, c)
    asd(b,a,c,n-1)

print(2 ** n - 1)
if n <= 20:
    asd(1,2,3,n)