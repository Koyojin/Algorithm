import math

k=int(input())

pcs=[]

if k in [2**i for i in range(21)]:
    print(k,0)
else:
    while k>0:
        for i in range(21):
            if 2**i==k:
                pcs.append(2**i)
                k-=2**i
                break
            
            elif 2**i>k:
                pcs.append(2**(i-1))
                k-=2**(i-1)
                break
            
    brks=math.log2(2*pcs[0]//pcs[len(pcs)-1])
    print(2*pcs[0],int(brks))
