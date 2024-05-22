import sys
sys.setrecursionlimit(100000)

n,m,t=map(int,input().split())
graph=[[0]*m for _ in range(n)]

for _ in range(t):
    y,x=map(int,input().split())
    graph[y-1][x-1]=1

count=0
result=[]

def dfs(x,y):
    global count
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    if 0<=x<m and 0<=y<n:
        if graph[y][x]==1:
            count+=1
            graph[y][x]=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs(nx,ny)

for i in range(m):
    for j in range(n):
        if graph[j][i]==1:
            dfs(i,j)
            result.append(count)
            count=0

print(max(result))