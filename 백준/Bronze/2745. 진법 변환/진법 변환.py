n,b=map(str,input().split())
con=0
cnt=0
for i in n[::-1]:
    if i.isupper():
        k=(int(b)**cnt)*(ord(i)-55)
    else:
        k=(int(b)**cnt)*int(i)
    con+=int(k)
    cnt+=1
print(con)