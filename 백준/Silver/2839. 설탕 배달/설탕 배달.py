n=int(input())
R=[]
for i in range(2000):
    for j in range(2000):
        if 5*i+j*3==n:
            R.append(i+j)
        else:
            pass
if len(R)==0:
    print(-1)
else:
    print(min(R))