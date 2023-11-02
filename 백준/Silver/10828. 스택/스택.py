import sys
input=sys.stdin.readline

n=int(input())
stack=[]
def command(k):
    if k.startswith('size'):
        print(len(stack))
    if k.startswith('e'):
        if stack==[]:
            print(1)
        else:
            print(0)
    if k.startswith('t'):
        if stack==[]:
            print(-1)
        else:
            print(stack[len(stack)-1])
    if k.startswith('po'):
        try:
            print(stack.pop())
        except:
            print(-1)
    if k.startswith('push'):
        stack.append(k.split()[1])

for i in range(n):
    x=input()
    command(x)
  