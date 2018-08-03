def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)
def inorder_without_recursion(root):
	current=root
	done=0
	stack=[]
	while not done:
		if current!=None:
			stack.append(current)
			current=current.left
		else:
			if len(stack)>0:
				current=stack.pop()
				print(current.data,end=" ")
				current=current.right
			else:
				done =1

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
print('inorder with recursion')
inorder(root)
print("")
print('inorder without recursion')
inorder_without_recursion(root)
print("")