import sys
input = sys.stdin.readline

n = int(input())
list = [input().split()]

def check(a,b,symbol):
    if symbol=='>':
        return a>b
    elif symbol=='<':
        return a<b

