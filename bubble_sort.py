# swap first two then 2 and 3rd then 3rd and 4th do again this process
a=[5,2,7,8,1]
n=len(a)
i=0
j=0
while i < n:
      while j < n-i-1:
            if a[j] > a[j+1]:
	       t=a[j]
	       a[j]=a[j+1]
	       a[j+1]=t
	    j+=1
      i+=1
      j=0 
print(a)
