import sys
input=sys.stdin.readline

n=int(input())
def rev(s):
    stack=s.split()
    for i in stack:
        k=list(i)
        k.reverse()
        a=''.join(k)
        print(a,end=' ')
for i in range(n):
    s=input().rstrip()
    rev(s)