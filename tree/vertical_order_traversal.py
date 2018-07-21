def printverticalline(root,line,hd):
    if root==None:
        return
    if hd==line:
        print(root.data, end=" ")
    printverticalline(root.left,line,hd-1)
    printverticalline(root.right,line,hd+1)


def findminmax(root,min,max,hd):
    if root==None:
        return
    if hd<min[0]:
        min[0]=hd
    elif hd>max[0]:
        max[0]=hd
    findminmax(root.left,min,max,hd-1)
    findminmax(root.right,min,max,hd+1)

def vertical_order_traversal(root):
    min=[0]
    max=[0]
    findminmax(root,min,max,0)
    for line in range(min[0],max[0]+1):
        printverticalline(root,line,0)


class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.right.left = Node(15)
root.left.right.left.right = Node(19)
vertical_order_traversal(root)
print("")
