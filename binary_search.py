#be careful of identation remember we will use recursion 3 times in every if we will just print that element exist of not

def binarysearch(a, j, r, x):
   if r >= 1:
      mid=j+(r-1)//2
      if x==mid:
         return mid
      if x>mid:
         return binarysearch(a, mid+1, r, x)
      if x<mid:
	 return binarysearch(a, 1, mid-1, x)
   else:
       return -1
a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
r=len(a)
x=input("enter a element to search:")
result=binarysearch(a, 1, r, x)
if result == -1:
   print("no")
else :
     print("yes, element exist")

