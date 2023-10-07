import sys
T=[]
n=int(input())
for i in range(n):
    T.append(int(sys.stdin.readline()))
M=[]
for i in range(n-1):
    M.append(T[i+1]-T[i])

def gcd_(a,b):
    while b>0:
        a,b=b,a%b
    return a
def gcd_N(arr):
    gcd=arr[0]
    for i in arr:
        gcd=gcd_(gcd,i)
    return gcd

k=gcd_N(M)
print(int(sum(M)/k-n+1))