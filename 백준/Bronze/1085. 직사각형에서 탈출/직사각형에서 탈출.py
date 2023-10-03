x,y,w,h=map(int,input().split())
if x<=w and y<=h:
    print(min([x,y,w-x,h-y]))
else:
    print(min([x-w,y-h,((x-m)**2+(y-h)**2)*(1/2)]))