n=int(input())
dpzero=[0]*(n+1)
dpone=[0]*(n+1)
for i in range(1,n+1):
    if i==1:
        dpzero[i]=0
        dpone[i]=1
    else:
        dpzero[i]=dpzero[i-1]+dpone[i-1]
        dpone[i]=dpzero[i-1]
print(dpzero[n]+dpone[n])