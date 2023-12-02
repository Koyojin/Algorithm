
n=int(input())
arr=[0]*10001
for i in range(n):
    arr[i+1]=int(input())
dp=[0]*10001
dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[1]+arr[2],arr[1]+arr[3],arr[2]+arr[3])
for i in range(3,n+1):
    dp[i]=max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])

print(max(dp))