n=int(input())
arr=[0]
dp=[0]

for _ in range(n):
    a=int(input())
    arr.append(a)
    dp.append(a)

if n==1:
    print(arr[1])
else:
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]

    for i in range(3,n+1):
        dp[i]=max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2])

    print(dp[n])    
