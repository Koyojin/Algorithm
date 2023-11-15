def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def gcd_up(arr):
    gcd1=arr[0]
    for i in arr:
        gcd1=gcd(gcd1,i)
    return gcd1

n,s=map(int,input().split())
sis=list(map(int,input().split()))
dis=[]
for i in sis:
    dis.append(abs(i-s))

print(gcd_up(dis))