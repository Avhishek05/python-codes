def divide(a,c):
    count=0
    for i in range(len(a)):
        if c[0]/a[i]==int(c[0]/a[i]):
            count+=1
    if count>=c[1]:
        return True
    else:
        return False
            
        
            
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=[list(map(int,input().split())) for i in range(m)]
for i in range(m):
    if divide(a,b[i]):
        print('Yes')
    else:
        print('No')