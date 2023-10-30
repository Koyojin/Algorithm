import sys
input=sys.stdin.readline
n=int(input())
array=list(map(int,input().split()))
sort1=sorted(list(set(array)))

dic={sort1[i]:i for i in range(len(sort1))}
for i in array:
    print(dic[i],end=' ')