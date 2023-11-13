import sys
n=[1]*1000001

for i in range(2,int(1000001**0.5)+1):
    if n[i]:
        for j in range(2*i,1000001,i):
            n[j]=0

while 1:
    k=int(sys.stdin.readline())
    if k==0:
        break
    else:
        for i in range(3,k-2,2):
            if n[i]==1 and n[k-i]==1:
                print(f"{k} = {i} + {k-i}")
                break 