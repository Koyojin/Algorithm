import math
n=int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif distance==r1+r2 or distance==abs(r1-r2):
        print(1)
    elif distance<r1+r2 and distance>abs(r1-r2):
        print(2)
    elif distance>r1+r2 or distance<abs(r1-r2):
        print(0)