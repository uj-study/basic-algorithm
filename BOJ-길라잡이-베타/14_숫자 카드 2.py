import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

count = 0
def search(first, last, a, r):
    mid = (first + last) // 2
    if r == a[mid]:
        return a[first:last+1].count(r)
    elif r > a[mid]:
        return search(mid+1,last,a,r)
    else:
        return search(first,mid - 1,a,r)

q = {}

for r in a:
    first = 0
    last = n - 1
    if r not in q:
        q[r] = search(first,last,a,r)
print(' '.join(str(q[x]) if x in q else '0' for x in b))