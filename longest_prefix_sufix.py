def find(n):
    l=len(n)
    s=l//2
    e=l//2
    for i in range(l//2):
        if len(n)%2==0:
            m=n[s:]
            if m==n[:e]:
                t=m
                return t
            else:
                e-=1
                s+=1
        else:
            m=n[s+1:]
            if m==n[:e]:
                t=m
                return t
            else:
                e-=1
                s+=1

z=int(input())
for i in range(z):
    n=input()
    if n==len(n)*n[0]:
        print(len(n[1:]))
    else:
        t=find(n)
        if t:
            print(len(t))
        else:
            print(0)
        