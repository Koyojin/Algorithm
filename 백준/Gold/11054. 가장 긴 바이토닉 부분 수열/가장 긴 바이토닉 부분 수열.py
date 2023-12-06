

n=int(input())
arr=list(map(int,input().split()))
rev=arr[::-1]

dp_inc=[1]*n
dp_dec=[1]*n

for i in range(n):
    for j in range(i):
        if rev[i]>rev[j]:
            dp_dec[i]=max(dp_dec[i],dp_dec[j]+1)
        if arr[i]>arr[j]:
            dp_inc[i]=max(dp_inc[i],dp_inc[j]+1)

dp=[dp_inc[i]+dp_dec[n-i-1]-1 for i in range(n)]
print(max(dp))