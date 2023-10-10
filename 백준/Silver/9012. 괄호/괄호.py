
t=int(input())
for i in range(t):
    k=input()
    if len(k)%2!=0:
        print("NO")
    else:
        count=0
        while 1:
            k=k.replace("()",'')
            count+=1
            if len(k)==0:
                print("YES")
                break
            elif count>50:
                print("NO")
                break