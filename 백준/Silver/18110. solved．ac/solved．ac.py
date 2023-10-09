import sys
input = sys.stdin.readline
n=int(input())
if n==0:
    print(0)
else:
    L=[int(input()) for i in range(n)]
    t=round(n * 3 / 20 + 0.0000001)
    L.sort()
    avg=round((sum(L[t:n-t])/(n-2*t))+0.000001)
    print(avg)