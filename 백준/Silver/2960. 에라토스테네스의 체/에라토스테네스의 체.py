n,k=map(int,input().split())
L=[i for i in range(2,n+1)]

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

R=[]
for i in L:
    if is_prime_number(i)==True:
        a=1
        while a*i<=n:
            try: 
                if a*i in R:
                    pass
                else:
                    R.append(a*i)
                a+=1
            except:
                pass
print(R[k-1])
