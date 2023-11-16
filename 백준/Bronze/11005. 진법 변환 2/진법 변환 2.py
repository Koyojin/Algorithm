n,b=map(int,input().split())
arr=[]
res=[]
while n!=0:
    arr.append(n%b)
    n=n//b
for i in arr[::-1]:
    if i>=10:
        k=chr(55+i)
        res.append(k)
    else:
        res.append(i)
print(''.join(map(str,res)))