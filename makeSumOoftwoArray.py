
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
flag = False
n=(sum(a1)-sum(a2))/2
print (n)
for i in a1:
    for j in a2:
        if i-j == n:
            flag=True
if flag == True:
    print (1)







# Given two arrays of integers, write a program to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
# Example:
# Input:
# 2
# 6 4
# 4 1 2 1 1 2
# 3 6 3 3
# 4 4
# 5 7 4 6
# 1 2 3 8
# Output:
# 1
# 1
