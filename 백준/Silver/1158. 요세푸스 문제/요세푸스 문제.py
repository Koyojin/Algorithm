from collections import deque

n,k=map(int,input().split())
L=deque(range(1,n+1))
count=0
R=[]
while len(L)>0:
    count+=1
    if count%k!=0:
        L.append(L.popleft())
    else:
        R.append(L.popleft())
print(str(R).replace('[', '<').replace(']', '>'))
