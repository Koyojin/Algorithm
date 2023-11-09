from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
q=deque([])
def que(s):
    if s.startswith("push_b"):
        _,b=s.split()
        q.append(b)
    elif s.startswith("push_f"):
        _,b=s.split()
        q.appendleft(b)
    elif s.startswith("si"):
        print(len(q))
    elif s.startswith("e"):
        if len(q)==0:
            print(1)
        else:
            print(0)
    else:
        if len(q)==0:
            print(-1)
        else:
            if s.startswith("pop_f"):
                print(q.popleft())
            if s.startswith("pop_b"):
                print(q.pop())
            if s.startswith("f"):
                print(q[0])
            if s.startswith("b"):
                print(q[-1])
for i in range(n):
    s=input().rstrip()
    que(s)