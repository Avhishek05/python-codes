def find(a,n):
    l=len(a)
    b=[];c=[]
    count=1
    top=0
    i=0
    s=0
    while i<len(a):
        d=a.pop()
        flag=False
        if d==top+1:
            top+=1
            c.append(d)
            count+=1
            for i in range(len(b)):
                d=b[-1]
                if d==top+1:
                    flag=True
                    b.pop()
                    top+=1
                    c.append(d)
                    count+=1
        if not flag:
            b.append(d)
        # print(*b)    
    if l==len(c):
        print("YES",count+1)
    else:
        print("NO")
        
        
    
z=int(input())
for _ in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    find(a,n)