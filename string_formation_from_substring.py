def find(n):
    l=len(n)
    
    for j in range(l//2):
        a=n[:l//2-j]
        for i in range(1,l//len(a)+1):
            if (len(a))*i==l:
                if a*i==n:
                    print('True')
                    return
    print('False')
z=int(input())
for _ in range(z):
    n=input()
    find(n)