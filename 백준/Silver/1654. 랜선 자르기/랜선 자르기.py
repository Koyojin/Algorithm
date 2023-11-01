import sys
input=sys.stdin.readline
k,n=map(int,input().split())
lan=[]
for i in range(k):
    a=int(input())
    lan.append(a)

left=1
right=max(lan)

while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in range(k):
        cnt+=lan[i]//mid
    if cnt>=n:
        left=mid+1
    else:
        right=mid-1

print(right)
    