def find(a,a1):
    a.sort()
    j=0
    i=a1[0]-1
    while i>0 and j<a1[0]:
        if a[j]+a[i]==a1[1]:
            return True
        elif a[j]+a[i]>a1[1]:
            i=i-1
        else:
            j=j+1
    return False
        
    
z=int(input())
for _ in range(z):
    a1=list(map(int,input().split()))
    a=list(map(int,input().split()))
    if find(a,a1):
        print("Yes")
    else:
        print("No")