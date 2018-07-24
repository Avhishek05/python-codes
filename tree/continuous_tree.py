def iscontinuous(root):
	if root==None:
		return True
	if root.left==None and root.right==None:
		return True
	if root.left==None:
			return (abs(root.data-root.right.data)==1 and iscontinuous(root.right))
	if root.right==None:
			return (abs(root.data-root.left.data)==1 and iscontinuous(root.left))

	return abs(root.data-root.right.data)==1 and iscontinuous(root.right) and abs(root.data-root.left.data)==1 and iscontinuous(root.left)
class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None
root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.right.right = Node(5)
root.left.right = Node(3)
# root.right.left = Node(6)
# root.left.right.left = Node(15)
# root.left.right.left.right = Node(19)

if iscontinuous(root):
	print("Yes")
else:
	print("No")