d = {}
d['abhi']=22
d['harshul']=21
d['c']=24
print d
#print d.value
#print d.key()
for k,v in d.items():
    print k,":",v
del d['c']
print d
d.clear
print d
