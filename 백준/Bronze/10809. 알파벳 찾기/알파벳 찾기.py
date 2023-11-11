alpha=[-1]*26
s=input()
for i in s:
    index=ord(i)-ord('a')
    alpha[index]=s.find(i)

print(*alpha)