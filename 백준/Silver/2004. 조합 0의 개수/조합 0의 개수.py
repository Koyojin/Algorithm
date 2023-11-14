a,b=map(int,input().split())
def pac(n,t):
    cnt=0
    while n>=t:
        cnt+=n//t
        n//=t
    return cnt
cnt5=pac(a,5)-pac(b,5)-pac(a-b,5)
cnt2=pac(a,2)-pac(b,2)-pac(a-b,2)
print(min(cnt5,cnt2))