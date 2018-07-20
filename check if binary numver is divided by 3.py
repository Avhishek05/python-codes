#input
#2
#1001
#100


def find(a):
    b=int(a,2)
    if b%3==0:
        print(1)
    else:
        print(0)
z=int(input())
for i in range(z):
    a=input()
    find(a)