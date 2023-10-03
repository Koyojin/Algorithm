X=[]
Y=[]
A=[]
for i in range(3):
    x,y=input().split()
    X.append(x)
    Y.append(y)
for i in X:
    if X.count(i)==1:
        A.append(i)
for i in Y:
    if Y.count(i)==1:
        A.append(i)
print(" ".join(A))