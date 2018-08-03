def find(s,a,n):
    s1=list(s)
    for i in range(n):
        s1[i]=chr(ord(s1[i])+a[n-1-i])
        print(a[n-1-i])
        if ord(s1[i])>123:
        	s1[i]=chr(ord(s1[i])-26)
        s=''.join(s1)
    print(s)
s=input()
n=int(input())
a=list(map(int,input().split()))
find(s,a,n)
