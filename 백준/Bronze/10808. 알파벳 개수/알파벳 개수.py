alpha=[0]*26
s=input()
for i in s:
    index=ord(i)-ord('a')
    alpha[index]+=1

print(*alpha)