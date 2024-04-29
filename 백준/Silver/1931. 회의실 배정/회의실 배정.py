n = int(input())
count=1
arr = []

for i in range(0,n):
    a, b = map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0])) #정렬

start,end=arr[0]

for newstart, newend in arr[1:]:
    if newstart>=end:
        count+=1
        end=newend

print(count)