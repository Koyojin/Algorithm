import sys
input=sys.stdin.readline

dx=[-1,1,-1,1,-1,1,0,0]
dy=[1,-1,-1,1,0,0,-1,1]

def bfs(x,y):
    queue=[(x,y)]
    mapp[x][y]=0

    while queue:
        x,y=queue.pop(0)

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=a or ny<0 or ny>=b:
                continue

            if mapp[nx][ny]==1:
                queue.append((nx,ny))
                mapp[nx][ny]=0

while 1:
    cnt=0
    a,b=map(int,input().split())

    if a==0 and b==0:
        break

    mapp=[]
    for i in range(b):
        xl=list(map(int,input().split()))
        mapp.append(xl)
    mapp=list(map(list,zip(*mapp)))

    for i in range(a):
        for j in range(b):
            if mapp[i][j]==1:
                bfs(i,j)
                cnt+=1
          

    print(cnt)