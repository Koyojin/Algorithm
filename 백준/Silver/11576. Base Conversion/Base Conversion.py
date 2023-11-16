a,b=map(int,input().split())
m=int(input())
arr=list(map(int,input().split()))
cnt=0
ar=0
for i in arr[::-1]:
    ar+=(a**cnt)*i
    cnt+=1
res=[]
while ar!=0:
    res.append(ar%b)
    ar//=b

print(*res[::-1])