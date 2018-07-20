t=int(input())
s=int(input())
b=list(map(int,input().split()))
a=[[b[j+s*i] for j in range(s)]for i in range(s)]
