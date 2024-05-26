from collections import deque
n=int(input())

dx=[-1,1,-1,1,-2,2,-2,2]
dy=[-2,2,2,-2,1,1,-1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

                if nx==ax and ny==ay:
                    return (graph[ax][ay])

for _ in range(n):
    l=int(input())
    graph=[[0]*l for _ in range(l)]
    
    ix,iy=map(int,input().split())
    ax,ay=map(int,input().split())
    
    if ix==ax and iy==ay:
        print(0)
    else:
        result=bfs(ix,iy)
        print(result)
