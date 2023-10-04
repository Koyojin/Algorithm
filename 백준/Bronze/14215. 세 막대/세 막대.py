L=sorted(list(map(int,input().split())))
if 2*L[2]>=sum(L):
    print(2*(L[1]+L[0])-1)
else:
    print(sum(L))
