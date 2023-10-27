import sys
input=sys.stdin.readline
def prime(n):
    global pl
    pl=[1]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if pl[i]==1:
            j=2
            while i*j<=n:
                pl[i*j]=0
                j+=1

prime(123456*2)

while 1:
    k=int(input())

    if k==0:
        break

    print(sum(pl[k+1:2*k+1]))

    