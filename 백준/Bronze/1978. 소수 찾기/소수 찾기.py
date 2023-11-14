prime=[0,0]+[1]*999

for i in range(2,int(1000**0.5)+1):
    if prime[i]==1:
        for j in range(2*i,1001,i):
            prime[j]=0

n=input()
t=list(map(int,input().split()))
cnt=0
for i in t:
    if prime[i]==1:
        cnt+=1
print(cnt)
