n=int(input())
stack=[]
r=[]
now=1
err=0

for i in range(n):
    k=int(input())
    while now<=k:
        stack.append(now)
        r.append('+')
        now+=1
    if stack[-1]==k:
        stack.pop()
        r.append('-')
    else:
        err=1
        break

if err==0:
    for i in r:
        print(i)
else: print("NO")