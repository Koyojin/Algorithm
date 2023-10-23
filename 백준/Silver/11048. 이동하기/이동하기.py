n,m=map(int,input().split())
graph=[[0]*(m+1)]+[([0]+list(map(int,(input().split())))) for i in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]

for x in range(1,n+1):
    for y in range(1,m+1):
        if x==1 and y==1:
            dp[x][y]=graph[x][y]
        elif x==1:
            dp[x][y]=graph[x][y]+dp[x][y-1]
        elif y==1:
            dp[x][y]=graph[x][y]+dp[x-1][y]
        else:
            dp[x][y]=max(dp[x-1][y-1],dp[x-1][y],dp[x][y-1])+graph[x][y]

print(dp[n][m])