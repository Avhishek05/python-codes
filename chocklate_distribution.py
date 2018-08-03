def find(a,n,m):
    b=[]
    a.sort()
    diff=float('inf')
    for i in range(n-m+1):
        dif=a[i+m-1]-a[i]
        if dif<=diff:
            b=a[i:i+m]
            diff=dif
    if len(b)==0:
        print(0)
        return
    print(max(b)-min(b))
    
z=int(input())
for _ in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    find(a,n,m)