cal=list(input())
stack=[]
res=''
ops=['(',')','*','/','+','-']
for i in cal:
    if i not in ops:
        res+=i
    else:
        if i=='(':
            stack.append(i)
        elif i=='*' or i=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # ( 괄호 제거
while stack:
    res+=stack.pop()

print(res)

            