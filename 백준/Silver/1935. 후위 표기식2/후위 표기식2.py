n=int(input())
cal=list(input())
ops=['*','+','-','/']
stack=[]
ab=[]*n
for i in range(n):
    ab.append(input())

for i in cal:
    if i in ops:
        a=stack.pop()
        b=stack.pop()
        r="("+b+i+a+")"
        stack.append(r)

    else:
        num=ord(i)-ord('A')
        stack.append(ab[num])
result=eval(stack[0])
print('%.2f'%result)


