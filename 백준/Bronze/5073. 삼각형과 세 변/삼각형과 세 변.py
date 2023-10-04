import sys
while 1:
    L=list(map(int,sys.stdin.readline().split()))
    if set(L)=={0}:
        break
    if 2*max(L)>=sum(L):
        print("Invalid")
    elif len(set(L))==1:
        print("Equilateral")
    elif len(set(L))==2:
        print("Isosceles")
    elif len(set(L))==3:
        print("Scalene")  