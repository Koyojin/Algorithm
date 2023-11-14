n=int(input())
res=1
cnt=0
for i in range(1,n+1):
    res*=i

for i in list(str(res))[::-1]:
    if i=='0':
        cnt+=1
    else:
        break

print(cnt)
