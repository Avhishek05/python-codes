def mirror(root):
	if root==None:
		return
	mirror(root.left)
	mirror(root.right)
	root.left,root.right=root.right,root.left

def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)
class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
#root.right.right = Node(7)
root.left.right = Node(5)
#root.right.left = Node(6)
# root.left.right.left = Node(15)
# root.left.right.left.right = Node(19)

print('before  inorder')
inorder(root)
print("")
mirror(root)
print('after inorder')
inorder(root)
print("")