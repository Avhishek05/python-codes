import itertools
a=[10, 1 ,2, 7, 6, 1, 5]
b=[]
for i in range(len(a)):
	for s in itertools.combinations(a,i):
		if s not in b:
			b.append(list(s))
print(b)
