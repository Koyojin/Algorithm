n=input()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
As=sorted(A)[::-1]
Bs=sorted(B)
R=[x*y for x,y in zip(As,Bs)]
print(sum(R))