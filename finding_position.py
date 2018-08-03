# Some people are standing in a queue. A selection process follows a rule where people standing on even positions 
# are selected. Of the selected people a queue is formed and again out of these only people on even position are 
# selected. This continues until we are left with one person. Find out the position of that person in the original
#  queue.
# input
# 1
# 5

def find(n):
    for i in range(n):
        if math.log(n-i,2)==int(math.log(n-i,2)):
            print(n-i)
            return
    
z=int(input())
for i in range(z):
    n=int(input())
    find(n)