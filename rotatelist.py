def rotate(a,l):
    return a[l:] + a[:l]
    
z=int(input())
for i in range(z):
    a1=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a=rotate(a,a1[1])
    print(*a)