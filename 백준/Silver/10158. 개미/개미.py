w,h=map(int,input().split())
x,y=map(int,input().split())
t=int(input())
a=(x+t)//w
b=(y+t)//h
if a%2==0:
    xr=(x+t)%w
else:
    xr=w-(x+t)%w
if b%2==0:
    yr=(y+t)%h
else:
    yr=h-(y+t)%h

print(xr,yr)