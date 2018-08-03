def isoperator(char):
	if char=='+' or char=='-' or char=='*' or char=='/' or char=='^':
		return True
	return False
def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)
class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

postfix="ab+ef*g*-"
root=constructtree(postfix)
print("your inorder is ")
inorder(root)