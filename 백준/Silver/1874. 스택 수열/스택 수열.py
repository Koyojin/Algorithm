n=int(input())
stack=[]
R=[]
strt=1
b=1

for i in range(n):
    k=int(input())

    while strt<=k:
        stack.append(strt)
        R.append('+')
        strt+=1
    
    if stack[-1]==k:
        stack.pop()
        R.append('-')
    
    else:
        b=0

if b==0:
    print('NO')
else:
    for i in R:
        print(i)