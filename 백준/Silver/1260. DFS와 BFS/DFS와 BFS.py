from collections import deque
n,m,v=map(int,input().split())
graph=[[0]*(n+1) for i in range((n+1))]

for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1

dv=[0]*(n+1)
bv=[0]*(n+1)

def dfs(v):
    dv[v]=1
    print(v,end=' ')
    for i in range(n+1):
        if not dv[i] and graph[v][i]==1:
            dfs(i)
def bfs(v):
    q=deque([v])
    bv[v]=1
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if not bv[i] and graph[v][i]==1:
                q.append(i)
                bv[i]=1
dfs(v)
print()
bfs(v)