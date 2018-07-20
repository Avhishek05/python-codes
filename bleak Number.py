# Input:
# 3
# 4
# 167
# 3


def find(n):
    c=0
    j=0
    for i in range(1,n):
        j=i+bin(i).count("1")
        #print("(",n,j,")")
        if n==j:
            print(0)
            return
    print(1)
z=int(input())
for i in range(z):
    n=int(input())
    find(n)