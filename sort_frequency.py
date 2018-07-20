def sort(a,l):
    b=list(set(a))
    c=[]
    for i in range(len(b)):
        c.append(a.count(b[i]))
    d=[]
    for i in range(len(b)):
        d.append([b[i],c[i]])
        d=sorted(d,key=lambda x: x[1],reverse=True)
        j=0
    for i in d:
        for j in range(i[1]):
            print(i[0],end=" ")
            j+=1
            if j==l:
                break
n=int(input())
l=input()
for i in range(n):
    a=list(map(int,input().split()))
    sort(a,l)
    
