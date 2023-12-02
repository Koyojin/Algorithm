import sys
input=sys.stdin.readline
n=int(input())

tree=[[0]*(n) for i in range(n)]

for i in range(n):
    tree[i]=list(map(int,input().split()))+[0]*(n-i-1)

for i in range(1,n):
    for j in range(n):
        if j==0:
            tree[i][j]+=tree[i-1][j]
        elif j==i:
            tree[i][j]+=tree[i-1][j-1]
        else:
            tree[i][j]+=max(tree[i-1][j-1],tree[i-1][j])

print(max(tree[n-1]))