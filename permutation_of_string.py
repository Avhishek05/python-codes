#input
#1
#ABC
import itertools
def find(n):
    n=list(n)
    n.sort()
    b=[]
    b=list(map("".join, itertools.permutations(n)))
    print(b)
    
z=int(input())
for i in range(z):
    n=input()
    find(n)