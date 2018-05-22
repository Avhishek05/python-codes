# compare 1 st element with rest and take minimum at first ,  compare 2nd element with rest and #take minimum to 2nd place continue this process, in this we find index of minimum element and use #it to swap
a=[5,2,7,8,1,67,3]
n=len(a)
i=0
m = 0
while i < n:
      j = i + 1
      m = i
      while j < n:
            if a[m] > a[j]:
               m = j
            j+=1	       
      t=a[i]
      a[i]=a[m]
      a[m]=t    
      i+=1
print(a)
