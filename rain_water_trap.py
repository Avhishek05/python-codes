def find(a,n):
    if n<3:
        print(0)
        return
    sum=0
    t=0
    for i in range(1,n-1):
        t=min(max(a[:i]),max(a[i+1:n]))-a[i]
        if t<0:
            t=0
        sum+=t
    if sum<0:
        print(0)
        return
    print(sum)
    
z=int(input())
for _ in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    find(a,n)