from collections import deque
s=input()
sq=deque(s)
res=[s]
for i in range(len(s)-1):
    sq.popleft()
    res.append(''.join(list(sq)))
res.sort()
for i in res:
    print(i)
