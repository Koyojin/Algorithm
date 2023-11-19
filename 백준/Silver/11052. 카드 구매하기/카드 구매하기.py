n=int(input())
card=[0]+list(map(int,input().split()))

p=[0]*(n+1)
for i in range(1,n+1):
    for k in range(1,i+1):
        p[i]=max(p[i],card[k]+p[i-k])
        
print(p[n])