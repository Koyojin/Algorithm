n=int(input())
dp=[-1001]+[0]*n
lst=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    dp[i]=max(dp[i-1]+lst[i],lst[i])
print(max(dp))