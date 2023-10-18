t=int(input())
for i in range(t):
    n=int(input())
    P=[0,1,1,1,2,2,3,4,5,7,9]+[0]*(n-10)
    for i in range(1,n+1):
        if i<9:
            pass
        else:
            P[i]=P[i-1]+P[i-5]
    print(P[i])