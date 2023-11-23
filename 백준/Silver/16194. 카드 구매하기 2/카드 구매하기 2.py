n=int(input())
card=[0]+list(map(int,input().split()))

p=[10000,card[1]]+[10000]*(n-1)
for i in range(1,n+1):
    for k in range(1,i+1):
        p[i]=min(card[i],card[k]+p[i-k],p[i])
print(p[n])