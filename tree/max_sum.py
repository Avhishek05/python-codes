
def height(root):
    if root==None:
        return 0
    else:
        h_l=height(root.left)
        h_r=height(root.right)
        b.append(root.data)

        if h_l>h_r:
            return h_l+1
        else:
            return h_r+1

class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None
b=[]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.right.left = Node(15)
root.left.right.left.right = Node(19)
print(height(root))
print (b)
