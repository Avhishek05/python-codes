n=17
n = n - 1
line = [1]
for k in range(max(n ,0)):
    line.append(line[k]*(n-k)//(k+1))
print(line)
