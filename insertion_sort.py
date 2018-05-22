# sort like playing cards
# asumw second element as a key if key is less than first element shift all element before key
#ahed and insert key at its right place 
a=[5,2,7,8,1,67,3]
n=len(a)
i=1
j=1
while i < n:
      key=a[i]
      j=i-1
      while j>=0 and key < a[j]:
	    a[j+1]=a[j]
            j-=1
      a[j+1]=key 
      i+=1	    	       
print(a)
