import sys
input=sys.stdin.readline


pre=1000000
pl=[1]*(pre+1)
for i in range(2,int((pre+1)**0.5)+1):
    if pl[i]:
        for j in range(2*i,pre+1,i):
            pl[j]=0

n=int(input())

for i in range(n):
    k=int(input())
    cnt=0
    for i in range(2,k//2+1):
        if pl[i] and pl[k-i]:
            cnt+=1
    print(cnt)