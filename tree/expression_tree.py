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
def constructtree(postfix):
	stack=[]
	for char in postfix:
		if not isoperator(char):
			t=Node(char)
			stack.append(t)
		else:
			t=Node(char)
			t1=stack.pop()
			t2=stack.pop()
			t.right=t1
			t.left=t2
			stack.append(t)
	t=stack.pop()
	return t

class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

postfix="ab+ef*g*-"
root=constructtree(postfix)
print("your inorder is ")
inorder(root)