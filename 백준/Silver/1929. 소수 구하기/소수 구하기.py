import sys

def prime(n):
    is_prime=[0,0]+[1]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
            for k in range(i*2,n+1,i):
                is_prime[k]=0

    return primes

m,n=map(int,input().split())
primes=prime(n)
for i in primes:
    if i>=m:
        print(i)