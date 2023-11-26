import sys
input=sys.stdin.readline

n=int(input())
r,g,b=map(int,input().split())
R=[0,r]
G=[0,g]
B=[0,b]
dpR=[0,r]+[0]*(n-1)
dpG=[0,g]+[0]*(n-1)
dpB=[0,b]+[0]*(n-1)

for i in range(2,n+1):
    a,b,c=map(int,input().split())
    R.append(a)
    G.append(b)
    B.append(c)
    dpR[i]=min(R[i]+dpG[i-1],R[i]+dpB[i-1])
    dpG[i]=min(G[i]+dpR[i-1],G[i]+dpB[i-1])
    dpB[i]=min(B[i]+dpR[i-1],B[i]+dpG[i-1])

print(min(dpR[n],dpG[n],dpB[n]))