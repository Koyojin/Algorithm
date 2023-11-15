n=int(input())
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

for i in range(n):
    case=list(map(int,input().split()))
    ans=0
    for i in range(1,len(case)):
        for j in range(i+1,len(case)):
            ans+=gcd(case[i],case[j])
    print(ans)