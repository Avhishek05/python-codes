def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def find(n):
    print(fact(2*n)//(fact(n+1)*fact(n)))
    
z=int(input())
for i in range(z):
    n=int(input())
    find(n)