import collections
def deletedeep(root,temp1):
	de=collections.deque([])
	de.append(root)
	while len(de)!=0:
		temp=de.popleft()
		if temp.left:
			if temp.left==temp1:
				temp.left=None
				del(temp)
				return
			else:
				de.append(temp.left)
		if temp.right:
			if temp.right==temp1:
				temp.right=None
				del(temp)
				return
			else:
				de.append(temp.right)
def deletion(root,n):
	de=collections.deque([])
	de.append(root)
	while len(de)!=0:
		temp=de.popleft()
		if temp.data==n:
			key=temp
		if temp.left:
			de.append(temp.left)
		if temp.right:
			de.append(temp.right)
	x=temp.data
	print(x)
	deletedeep(root,temp)
	key.data=x


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
root.right.right = Node(7)
root.left.right = Node(5)
root.right.left = Node(6)
# root.left.right.left = Node(15)
# root.left.right.left.right = Node(19)
n=int(input('enter a node to delete'))
print('before deletion inorder')
inorder(root)
print("")
deletion(root,n)
print('after deletion inorder')
inorder(root)
print("")