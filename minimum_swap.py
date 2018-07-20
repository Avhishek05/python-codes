from collections import OrderedDict
def minSwaps(arr, n):
	a={}
	b={}
	for i in range(len(arr)):
		a[arr[i]]=i
	b=OrderedDict(sorted(a.items()))
	print(b)
	c=[False]*n
	ans=0
	d=list(b.keys())
	for i in range(n):
		if c[i] or b[d[i]]==i:
			continue
		cycle=0
		j=i
		while c[j]==False:
			c[j]=True
			j=b[d[j]]
			cycle+=1
		ans+=cycle-1
	return ans

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(minSwaps(arr, n))




