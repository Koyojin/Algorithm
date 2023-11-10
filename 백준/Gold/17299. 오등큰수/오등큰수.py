from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
count=Counter(arr)
res=[-1]*n
stack=[]

for i in range(n):
    while stack and count[arr[stack[-1]]]<count[arr[i]]:
        res[stack.pop()]=arr[i]
    stack.append(i)
  
print(' '.join(map(str,res)))
