a=[2,6,3,8,48,54]
n=len(a)
def partition(a,l,h):
    i=l-1
    pivot=a[h]
    for j in range(l,h):
        if a[j]< pivot:
           i+=1
           a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def quicksort(a,l,h):
    if l<h:
       p=partition(a,l,h)
       quicksort(a,0,p-1)
       quicksort(a,p+1,h)
quicksort(a,0,n-1)
print(a)
