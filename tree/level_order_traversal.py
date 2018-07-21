def height(root):
    if root==None:
        return 0
    else:
        h_l=height(root.left)
        h_r=height(root.right)
        if h_l>h_r:
            return h_l+1
        else:
            return h_r+1

def level_order_traversal(root,h):
    for i in range(1,h+1):
        level_order(root,i)
def level_order(root,i):
    if root==None:
        return
    else:
        if i==1:
            print (root.data,end=" ")
        level_order(root.right,i-1)
        level_order(root.left,i-1)



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.left.right = Node(5)
root.right.left = Node(6)
h=height(root)
print("height is :",h)
level_order_traversal(root,h)
