# from itertools import combinations
def find(a):
    b=[]
    for i in range(1,len(a)+1):
        for j in range(i):
            # b.append(a[j])
            # b.append(a[j].upper())
            b.append(a[j:i])
            # b.append(a[j:i].upper())
    b=set(b)
    b=list(b)
    print(*b)
    # b.sort()
    # c="".join(b)
    # for i in range(1,len(a)+1):
        # print ("".join(d) for d in combinations(b, i))
#z=int(input())
# for i in range(z):
a='abc'
find(a)