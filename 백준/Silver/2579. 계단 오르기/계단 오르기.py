n=int(input())
mm=[0]*(n+1)
value=[0]*(n+1)

for i in range(1,n+1):
    value[i]=int(input())

if n==1:
    print(value[1])
    exit()

elif n==2:
    print(value[1]+value[2])
    exit()

mm[1]=value[1]
mm[2]=value[1]+value[2]

for i in range(3,n+1):
    mm[i]=value[i]+max(mm[i-2],mm[i-3]+value[i-1])

print(mm[-1])