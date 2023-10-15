import math
a,b=map(int,input().split())
c,d=map(int,input().split())
nume=a*d+c*b
deno=b*d
k=math.gcd(nume,deno)
print(int(nume/k),int(deno/k))