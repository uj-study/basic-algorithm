import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split())).sort()
m = int(input())
b = list(map(int, input().split()))

count = 0

for i in b:
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) / 2
        if i == a[mid]:
            count += 1
        elif i > a[mid]:
            first = mid + 1
        else:
            last = mid - 1
    
    if count == 0:
        print(0)
    else:
        print(count)