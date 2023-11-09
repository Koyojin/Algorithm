from collections import deque
ans=''
tag=0
stack=''
for i in input():
    if i=='<':
        tag=1
        ans+=stack[::-1]
        stack=''
        ans+=i
        continue
    
    elif i=='>':
        tag=0
        ans+=i
        continue

    elif i==" ":
        ans+=stack[::-1]+" "
        stack=""
        continue

    if tag:
        ans+=i
    else:
        stack+=i
print(ans+stack[::-1])