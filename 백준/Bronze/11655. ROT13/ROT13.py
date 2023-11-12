s=input()
res=[]
for i in s:
    if i.isupper():
        if ord(i)<=77:
            k=ord(i)+13
        elif ord(i)>77:
            k=ord(i)-13
        res.append(chr(k))
    elif i.islower():
        if ord(i)<=109:
            k=ord(i)+13
        elif ord(i)>109:
            k=ord(i)-13
        res.append(chr(k))
    else:
        res.append(i)
print(''.join(res))