t=int(input())
for i in range(t):
    n=int(input())
    L=[0]*(n+1)

    for i in range(1,n+1):
        if i==1:
            L[i]=1
        elif i==2:
            L[i]=2
        elif i==3:
            L[i]=4
        else:
            L[i]=L[i-1]+L[i-2]+L[i-3]
    print(L[n])