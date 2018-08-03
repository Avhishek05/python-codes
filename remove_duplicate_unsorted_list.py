def find(a,n):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(*b)
    
z=int(input())
for _ in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    find(a,n)