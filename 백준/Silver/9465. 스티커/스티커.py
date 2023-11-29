import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):

    n=int(input())

    arr=[[0]*(n+1)]
    dp=[[0]*(n+1) for _ in range(3)]
    arr.append([0]+list(map(int,input().split())))
    arr.append([0]+list(map(int,input().split())))

    if n==1:
        print(max(arr[1][1],arr[2][1]))
        

    else:
        dp[1][1],dp[2][1]=arr[1][1],arr[2][1]
        dp[1][2],dp[2][2]=dp[2][1]+arr[1][2],dp[1][1]+arr[2][2]

        for i in range(3,n+1):
            dp[1][i]=max(dp[2][i-1],dp[2][i-2])+arr[1][i]
            dp[2][i]=max(dp[1][i-1],dp[1][i-2])+arr[2][i]        
            
        print(max(dp[1][n],dp[2][n]))